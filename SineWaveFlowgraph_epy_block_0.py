import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, freq_porteuse=4e6, freq_source=1e6, amplitude=2.0):
        gr.sync_block.__init__(
            self,
            name='Modulateur BPSK',
            in_sig=[np.float32],       # flux NRZ bipolaire (-1, +1)
            out_sig=[np.float32]       # signal BPSK réel (tension)
        )
        self.freq_porteuse = freq_porteuse
        self.freq_source = freq_source
        self.amplitude = amplitude
        self.phase = 0.0   # phase persistante entre les appels

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        n = len(in0)

        # vecteur temps local, décalé de la phase accumulée
        t = np.arange(n) / self.freq_source
        carrier = self.amplitude * np.cos(2 * np.pi * self.freq_porteuse * t + self.phase)

        # symbole=+1 -> phase 0° (en phase) ; symbole=-1 -> phase 180° (opposition de phase)
        out[:] = in0 * carrier

        # mise à jour de la phase pour le prochain appel (continuité)
        self.phase += 2 * np.pi * self.freq_porteuse * n / self.freq_source
        self.phase = np.mod(self.phase, 2 * np.pi)  # évite l'overflow numérique

        return n