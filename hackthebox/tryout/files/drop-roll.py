from pwn import *

r = remote('94.237.62.240', 45066)

r.recvuntil(b'(y/n) ')

r.sendline(b'y')

r.recvuntil(b'\n')

tries = 0

while True:
    try:
        got = r.recvline().decode()
        payload = got.replace(", ", "-").replace("GORGE", "STOP").replace("PHREAK", "DROP").replace("FIRE", "ROLL").strip()

        r.sendlineafter(b'What do you do?', payload.encode())
        tries = tries + 1
        log.info(f'{tries}: {payload}')
    except EOFError:
        log.success(got.strip())
        r.close()
        break