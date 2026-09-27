import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, freq_porteuse=10e3, freq_source=1e6, bit_rate=1e3):
        gr.sync_block.__init__(
            self,
            name='Modulateur BPSK',
            in_sig=[np.int8],   # bits 0/1
            out_sig=[np.float32]
        )
        self.fp = freq_porteuse
        self.fs = freq_source
        self.Rb = bit_rate

        self.samples_per_bit = int(self.fs / self.Rb)
        self.phase = 0

    def work(self, input_items, output_items):
        bits = input_items[0]
        out = output_items[0]

        # NRZ
        nrz = 2*bits - 1

        # Upsampling
        nrz_up = np.repeat(nrz, self.samples_per_bit)

        n = len(nrz_up)
        t = np.arange(n) / self.fs

        carrier = np.cos(2*np.pi*self.fp*t + self.phase)

        out[:n] = nrz_up * carrier

        self.phase += 2*np.pi*self.fp*n/self.fs
        self.phase = np.mod(self.phase, 2*np.pi)

        return n