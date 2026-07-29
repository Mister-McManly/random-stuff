symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def my_base64EP(data : bytes):
    output=""
    bits=""
    chunk_size = 6
    for byte in data:
        bits += format(byte, '08b')
    three_bytes = len(bits)%24
    padding = 6 - len(bits)%6
    bits += "0" * padding
    chunks = [bits[i:i + chunk_size] for i in range(0, len(bits), chunk_size)]
    for chunk in chunks:
        output += symbols[int(chunk,2)]
    if three_bytes == 0:
        pass
    elif three_bytes == 16:
        output += "="
    elif three_bytes == 8:
        output += "=="
    return output
    

def hex_to_bytes(hex_data):
    return(bytes.fromhex(hex_data))

if __name__=="__main__":
    word = input("Please input your name: ")
    ascii_bytes = (bytes(word,"ascii"))
    #our_data = hex_to_bytes("abcdABCD0123456789")
    print(my_base64EP(ascii_bytes))