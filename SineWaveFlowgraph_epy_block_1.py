import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, echantillons_sec=128):
        gr.sync_block.__init__(
            self,
            name='Mapping Phase BPSK',
            in_sig=None,
            out_sig=[np.complex64]
        )
        self.symbols = [-1, +1]

    def work(self, input_items, output_items):
        out = output_items[0]
        n = len(out)
        index = 0
        for i in range(n):
            out[i] = self.symbols[index]
            index = (index + 1) % len(self.symbols)
        return len(out)