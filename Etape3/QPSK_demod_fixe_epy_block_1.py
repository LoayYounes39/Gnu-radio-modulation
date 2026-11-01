import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Mapping 4PSK',
            in_sig=[np.uint8],
            out_sig=[np.complex64]
        )
        # Mapping Gray : bit de poids fort -> I, bit de poids faible -> Q
        self.dico = {
            0: 1+1j,    # 00
            1: 1-1j,    # 01
            2: -1+1j,   # 10
            3: -1-1j    # 11
        }

    def work(self, input_items, output_items):
        symboles = input_items[0]
        out = output_items[0]

        for i, s in enumerate(symboles):
            out[i] = self.dico[int(s)]

        return len(out)
