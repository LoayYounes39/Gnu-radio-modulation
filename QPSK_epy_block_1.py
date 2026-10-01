import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, echantillons_sec=128):
        gr.sync_block.__init__(
            self,
            name='Mapping Phase QPSK',
            in_sig=[np.int32],      
            out_sig=[np.complex64]
        )
        self.symbols = [1+1j, -1+1j, 1-1j, -1-1j] 

    def work(self, input_items, output_items):
        in0 = input_items[0]  
        out = output_items[0]         
        for i in range(len(in0)):
            out[i] = in0[i]
            
        return len(out)