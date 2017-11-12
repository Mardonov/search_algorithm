# -*- coding:utf-8 -*-
import struct

XTMP_STRUCT = 'hi32s4s32s256shhiii4i20x'
XTMP_STRUCT_SIZE = struct.calcsize(XTMP_STRUCT)


def read_xtmp(fname):
    result = []
    fp = open(fname, 'rb')
    while True:
        bytes = fp.read(XTMP_STRUCT_SIZE)
        if not bytes:
            break
        data = struct.unpack(XTMP_STRUCT, bytes)
        data = [(lambda s: str(s).split("\0", 1)[0])(i) for i in data]
        if data[0] != '0':
            result.append(data)
    fp.close()
    result.reverse()
    return result


print('reading data from utmp')
data = read_xtmp('/var/run/utmp')
for i in data:
    print(i)
print('=========================')
print('reading data from wtmp')
data = read_xtmp('/var/log/wtmp')
for i in data:
    print(i)
