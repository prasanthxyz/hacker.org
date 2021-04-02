# Get pi-billion.txt from https://stuff.mit.edu/afs/sipb/contrib/pi/

to_check = '12345678'
result = 0
idx = -20
with open('pi-billion.txt') as f_pi_bil:
    var_to_check = 'xxxxxxxxxxxxxxxxxxxx'
    cnt = 0
    while True:
        data = f_pi_bil.read(10)
        if not data:
            break
        var_to_check = var_to_check[10:] + data
        idx += 10
        chk = var_to_check.find(to_check)
        if chk != -1:
            result = chk + idx
            break

print(result-1)
