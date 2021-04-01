import requests
import time

ctr = -1
with open('OneMinuteManSolution.txt', 'w') as of:
    while True:
        ctr += 1
        resp = requests.get('http://www.hacker.org/challenge/misc/minuteman.php')
        if 'back later' not in resp.text:
            print(resp.text)
        elif ctr % 15 == 0:
            print(str(ctr*20/60) + ' minutes passed out of 1440')
        of.writelines(resp.text)
        time.sleep(20)
