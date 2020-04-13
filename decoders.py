# coding=utf-8

import codecs
import base64
from Crypto.Util.number import bytes_to_long, long_to_bytes

import json
from pwn import *


def decode_json(input_json):
    json_obj = json.loads(input_json)

    try:
        encoding = json_obj['type']
    except KeyError:
        flag  =json_obj['flag']
        print(flag)
        exit()

    encoded = json_obj['encoded']

    if encoding == "base64":
        return base64.b64decode(encoded).decode()
    elif encoding == "hex":
        return bytes.fromhex(encoded).decode('utf-8')
    elif encoding == "rot13":
        return codecs.decode(encoded, 'rot_13')
    elif encoding == "bigint":
        return long_to_bytes(int(encoded, 16)).decode('utf-8')
    elif encoding == "utf-8":
        return ''.join([chr(x) for x in encoded])


def main():
    host = 'socket.cryptohack.org'
    port = 13377

    conn = remote(host, port)
    while True:
        json_input = conn.recvline()
        response = decode_json(json_input)
        conn.send(json.dumps({'decoded': response}))


if __name__ == "__main__":
    main()
