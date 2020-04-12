# coding=utf-8

import sys

import codecs
import base64
import Crypto.Util.number

import json
from pwn import *

def ascii_decoder(_input):
    str_arr = [chr(x) for x in _input]
    return ''.join(str_arr)


def hex_decoder(_input):
    return bytes.fromhex(_input)


def base64_bytes_encoder(_input):
    return base64.encodebytes(_input)


def encode_long_to_bytes(_int):
    return Crypto.Util.number.long_to_bytes(_int)


def encode_bytes_to_long(_bytes):
    return Crypto.Util.number.bytes_to_long(_bytes)


def encode_rot13(_input):
    return codecs.encode(_input, 'rot13')


def main(input_json):
    encoded = json.dumps(input_json["encoded"])
    print(encoded)


def make_a_connection(host, port):
    conn = remote(host, port)
    json_input = conn.recvline()
    print(json_input)
    conn.send('USER anonymous\r\n')
    conn.recvuntil(' ', drop=True)
    conn.recvline()
    conn.close()


if __name__ == "__main__":
    ascii_str = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    hex_str = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
    _base64 = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
    big_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

    #print(ascii_decoder(ascii_str).decode('utf-8'))

    #print(hex_decoder(hex_str).decode('utf-8'))

    # _bytes = hex_decoder(_base64)
    # print(base64_bytes_encoder(_bytes).decode('utf-8'))

    #print(encode_long_to_bytes(big_integer).decode('utf-8'))

    keep_on_going = True

    # while keep_on_going:
    #     main(sys.args[1])

    #     while True:
    #         input_ = raw_input('Type ENTER to continue, c to stop: ')
    #         if input_ == '':
    #             keep_on_going = True
    #             break
    #         elif input_ == 'c':
    #             keep_on_going = False
    #             break
    #         else:
    #             continue

    make_a_connection('socket.cryptohack.org', 13377)
