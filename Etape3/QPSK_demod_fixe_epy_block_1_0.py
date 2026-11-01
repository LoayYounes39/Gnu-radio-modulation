import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='4PSK symbole plus proche',
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )

    def work(self, input_items, output_items):
        x = input_items[0]
        out = output_items[0]

        for i, v in enumerate(x):
            # les 4 points sont dans les 4 quadrants : decision par le signe de I et de Q
            I = 1 if v.real >= 0 else -1
            Q = 1 if v.imag >= 0 else -1
            out[i] = complex(I, Q)

        return len(out)
