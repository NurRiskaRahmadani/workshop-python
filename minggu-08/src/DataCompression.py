import zlib
s = b'Whatever you want... Whatever you need....'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)