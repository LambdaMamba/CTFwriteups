from pwn import *
import time
import sys

io = process(['./pin_checker'])

context.arch = 'amd64'
gs = '''
continue
'''

#allow pin number to be inputted as argument, eg: python3 side.py 12345678
pin = str(sys.argv[1])

#send the pin as the input to the pin_checker
io.sendline(pin)
#skip first output, which is 'Please enter your 8-digit PIN code:'
io.recvline()
#skip second output, which is PIN length
io.recvline()
#skip third output, which is 'Checking PIN...'
io.recvline()
#start the timer
start = time.time()
#fourth output is 'Access denied.', we are measuring time until this is outputted
recevied4 = io.recvline()
#stop the timer
stop = time.time()
#calculate time difference
time_taken = stop - start

log.info(f"Time taken: {time_taken}")
log.info(f"Received4: {recevied4}")
log.info(f"Guess: {pin}")


sys.exit()
