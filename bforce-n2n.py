import time
import datetime

import itertools
import threading
import time
import sys

with open('n2n.txt') as f:
    guns = f.readlines()

for l in guns:
    print(l.rstrip("\n\r"))

print('Enter your N2N ID:')
x = input()
print('Enter password:')
y = input()

print('')

print('Enter your target ip:')
tgt = input()

print('')

print('Enter your wordlist location:')
z = input()

my_list     = []
my_list.append('ping (%s)' % (tgt))
my_list.append('ping (%s) 56(84) bytes of data'  % (tgt))
my_list.append('64 bytes nsa.gov (%s): icmp_req=1 ttl=11'  % (tgt))
my_list.append('1 packets transmitted. 1 received. 0% packet loss. time 0.')

for l in my_list:
    print(l)
    time.sleep(1)


done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rPreparing your wordlist ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
done = True
print('')
print('Done! Wordslist ready to use.')
print('List Count:9875894')
print('')

tm    = datetime.datetime.now();
print('Using your list in a minutes, ngopi dulu sana')
time.sleep(3)
strtime     = 'Starting time %s' % (tm)

print(strtime)


with open('Top304Thousand-probable-v2.txt') as f:
    wordl = f.readlines()

for idx, l in enumerate(wordl):

    if idx <= 5 :

        a   = wordl[idx].strip()
        b   = wordl[idx+100].strip()
        print("%s:3306 MYSQL - [%s/9875894] - Trying username:'%s' with password:'%s'" % (tgt, idx, b,a))
        time.sleep(1)
        print("%s:3306 MYSQL - [%s/9875894] - failed to login as '%s' with password:'%s'" % (tgt, idx, b,a))
        time.sleep(1)
    else :
        print('Destination host unreachable.')
        time.sleep(1)