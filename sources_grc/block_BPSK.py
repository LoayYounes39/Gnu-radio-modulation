import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, freq_porteuse=10e3, freq_sourcefs=1e6):
        gr.sync_block.__init__(
            self,
            name='Carrier Multiplier',
            in_sig=[np.complex64],     # signal en bande de base (I/Q)
            out_sig=[np.complex64]     # signal transposé (toujours complexe ici)
        )
        self.freq_porteuse = freq_porteuse
        self.freq_source = freq_source
        self.phase = 0.0   # phase persistante entre les appels

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        n = len(in0)

        # vecteur temps local, décalé de la phase accumulée
        t = np.arange(n) / self.freq_source
        carrier = np.exp(1j * (2 * np.pi * self.freq_porteuse * t + self.phase))

        # multiplication complexe : transposition en fréquence
        out[:] = in0 * carrier

        # mise à jour de la phase pour le prochain appel (continuité)
        self.phase += 2 * np.pi * self.freq_porteuse * n / self.freq_source
        self.phase = np.mod(self.phase, 2 * np.pi)  # évite l'overflow numérique

        return n