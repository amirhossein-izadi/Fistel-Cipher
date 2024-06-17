from utils import *
import random
class IFC:

    def __init__(self, master_key):
        self.master_key = master_key
        self.round_keys = self.generate_round_keys()

    def generate_round_keys(self):
        k = [0] * 8
        for i in range(8):
            k[i] = self.master_key[i * 32:(i + 1) * 32]

        rk = [0] * 32
        for i in range(4):
            for j in range(8):
                round_shift = k[j][j:] + k[j][:j]
                rk[8 * i + j] = int(round_shift, 2) ^ int(k[(j + 1) % 8], 2)
                rk[8 * i + j] = bin(rk[8 * i + j])[2:].zfill(32)
            k = rk[8 * i:8 * (i + 1)]

        round_keys = []
        for i in range(16):
            round_keys.append([rk[i], rk[31 - i]])

        return round_keys

    @staticmethod
    def initial_permutation(chunk):

        # Split the 128-bit input into two 64-bit halves
        left_half = chunk[:64]
        right_half = chunk[64:]
        # Apply the permutation to each half
        permuted_left = permute(left_half, IP)
        permuted_right = permute(right_half, IP)
        # Combine the permuted halves
        return permuted_left, permuted_right

    @staticmethod
    def final_permutation(lh, rh):
        permuted_left = permute(rh, FP)
        permuted_right = permute(lh, FP)
        return permuted_left + permuted_right

    @staticmethod
    def f(lh, rh, lsk, rsk):
        # split rh into two 32-bit halves
        lrh, rrh = lh[:32], lh[32:]

        # Left-right half process
        lrh = xor_bits(lrh, rrh)
        lrh = permute(lrh, LRP)

        # Right-right half process
        rrh = expansion_permutation(rrh)
        sk = contraction_permutation(lsk, rsk)
        rrh = xor_bits(rrh, sk)
        rrh = keyed_substitution(rrh)

        # output left
        next_rh = interleave(lrh, rrh)
        next_rh = xor_bits(lh, next_rh)

        # output right
        next_lh = rh

        return next_lh, next_rh

    def encrypt(self, plain_text):
        chunks = text_to_128bit_chunks(plain_text)

        cipher_text = ''

        for chunk in chunks:

            lh, rh = IFC.initial_permutation(chunk)
            for i in range(16):
                lsk, rsk = self.round_keys[i]
                lh, rh = IFC.f(lh, rh, lsk, rsk)

            cipher_chunk = IFC.final_permutation(lh, rh)
            cipher_text += cipher_chunk

        return cipher_text

def main():
    ifc = IFC(master_key=''.join(random.choice('0') for _ in range(256)))
    en = xor_bits(ifc.encrypt('0'), ifc.encrypt('1'))
    print(en)


if __name__ == '__main__' :
    main()




