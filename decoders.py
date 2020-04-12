def ascii_decoder(_input):
    str_arr = [chr(x) for x in _input]
    return ''.join(str_arr)

def hex_decoder(_input):
    hex_arr = []
    i = 0
    while i < len(_input):
        hex_arr.append(_input[i:i+2].decode('hex'))
        i += 2
    return ''.join(hex_arr)

def base64_decoder(_input):
    pass

if __name__ == "__main__":
    ascii_str = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    hex_str = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
    base64 = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

    _bytes = hex_decoder(base64)
    print(_bytes)
