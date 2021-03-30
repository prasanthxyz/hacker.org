numbers = [199, 77, 202]
bin_ = [bin(x)[2:].zfill(8) for x in numbers]
result = ''.join(bin_)
print(int(result, 2))
