import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Mapping IQ',
            in_sig=[np.uint8],
            out_sig=[np.float32, np.float32]
        )
        # index 2 bits -> niveau (Gray : 00->-3, 01->-1, 11->+1, 10->+3)
        self.levels = np.array([-3, -1, 3, 1], dtype=np.float32)

    def work(self, input_items, output_items):
        x = input_items[0]
        n = min(len(x), len(output_items[0]))
        output_items[0][:n] = self.levels[(x[:n] >> 2) & 0b11]   # I : groupe de gauche
        output_items[1][:n] = self.levels[x[:n] & 0b11]          # Q : groupe de droite
        return n