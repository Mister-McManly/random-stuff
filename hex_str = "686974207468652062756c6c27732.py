hex_str1 = "686974207468652062756c6c277320657965"
hex_str2 = "1c0111001f010100061a024b53535009181c"

bit_length = len(hex_str1) * 4

bin_str1 = f"{int(hex_str1, 16):0{bit_length}b}"
bin_str2 = f"{int(hex_str2, 16):0{bit_length}b}"

xor_bin_list = []
for bit1, bit2 in zip(bin_str1, bin_str2):
    xor_bit = str(int(bit1) ^ int(bit2))
    xor_bin_list.append(xor_bit)

final_bin_str = "".join(xor_bin_list)
final_hex = f"{int(final_bin_str, 2):x}"

print (final_hex)