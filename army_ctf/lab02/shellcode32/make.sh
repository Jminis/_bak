#!/bin/bash
gcc -m32 -c -o shellcode.o shellcode.S
objcopy -S -O binary -j .text shellcode.o shellcode.bin
rm -rf shellcode.o
gcc -m32 -c -o readflag.o readflag.S
objcopy -S -O binary -j .text readflag.o readflag.bin
rm -rf readflag.o
gcc -m32 -c -o test.o test.S
objcopy -S -O binary -j .text test.o test.bin
rm -rf test.o
