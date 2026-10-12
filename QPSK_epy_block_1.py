import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Mapping IQ',
            in_sig=[np.uint8],
            out_sig=[np.complex64]
        )
        # index 2 bits -> niveau (Gray : 00->-3, 01->-1, 10->+3, 11->+1)
        self.levels = np.array([-3, -1, 3, 1], dtype=np.float32)

    def work(self, input_items, output_items):
        x = input_items[0]
        n = min(len(x), len(output_items[0]))
        i_part = self.levels[(x[:n] >> 2) & 0b11]   # I : groupe de gauche (bits 3-2)
        q_part = self.levels[x[:n] & 0b11]          # Q : groupe de droite (bits 1-0)
        output_items[0][:n] = (i_part + 1j * q_part).astype(np.complex64)
        return n