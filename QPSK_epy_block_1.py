import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, echantillons_sec=128):
        gr.sync_block.__init__(
            self,
            name='Mapping Phase QPSK',
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )

    def work(self, input_items, output_items):
        inp = input_items[0]   # <-- récupération de l'entrée
        out = output_items[0]
        n = len(out)
        index = 0
        for i in range(n):
            out[i] = inp[index]   # <-- utilisation de l'entrée
            index = index + 1

        return len(out)