# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import packbits

DATA = b'\xFE\xAA\x02\x80\x00\x2A\xFD\xAA\x03\x80\x00\x2A\x22\xF7\xAA'
RESULT = b'\xAA\xAA\xAA\x80\x00\x2A\xAA\xAA\xAA\xAA\x80\x00\x2A\x22\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA'

def test_decode():
    decoded = packbits.decode(DATA)
    assert decoded == RESULT

def test_encode_decode():
    encoded = packbits.encode(RESULT)
    decoded = packbits.decode(encoded)
    assert decoded == RESULT

def test_encode_empty():
    assert packbits.encode(b'') == b''

def test_encode_single():
    encoded = packbits.encode(b'X')
    assert encoded == b'\x00X'
    assert packbits.decode(encoded) == b'X'

def test_raw():
    encoded = packbits.encode(b'123')
    assert encoded == b'\x02123'
    assert packbits.decode(encoded) == b'123'

def test_encode2():
    encoded = packbits.encode(b'112112')
    assert packbits.decode(encoded) == b'112112'
    
def test_encode_switching_rle():
    encoded = packbits.encode(b'1122')
    assert packbits.decode(encoded) == b'1122'

def test_encode_long_rle():
    data = b'1' * 126
    encoded = packbits.encode(data)
    assert packbits.decode(encoded) == data

def test_encode_long_rle2():
    data = b'1' * 127
    encoded = packbits.encode(data)
    assert packbits.decode(encoded) == data

def test_encode_long_rle3():
    data = b'1' * 128
    encoded = packbits.encode(data)
    assert packbits.decode(encoded) == data

def test_restart_rle():
    data = b'1' * 127 + b'foo'
    encoded = packbits.encode(data)
    assert packbits.decode(encoded) == data

def test_encode_long_raw():
    data = b'12345678' * 17
    encoded = packbits.encode(data)
    print(encoded)
    assert packbits.decode(encoded) == data

def test_encode_long_raw():
    data = b'12345678' * 16
    encoded = packbits.encode(data)
    assert packbits.decode(encoded) == data

def test_encode_long():
    data = b'1' * 128 + b'12345678' * 17
    encoded = packbits.encode(data)
    assert packbits.decode(encoded) == data

