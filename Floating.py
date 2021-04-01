code = "1000001000010001010001011000000"

import struct
f = int(code, 2)
result = struct.unpack('f', struct.pack('I', f))[0]
print(round(result, 6))
