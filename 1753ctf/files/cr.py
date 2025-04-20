import hashlib

flag = [0x45,0x00,0x50,0x39,0x08,0x6f,0x4d,0x5b,0x58,0x06,0x66,0x40,0x58,0x4c,0x6d,0x5d,
        0x16,0x6e,0x4f,0x00,0x43,0x6b,0x47,0x0a,0x44,0x5a,0x5b,0x5f,0x51,0x66,0x50,0x57]

date = "2025-04-12"
hour = 2

for minute in range(49, 54):  # dari 02:49 s.d 02:53
    for second in range(0, 60):
        time = f"{hour:02}:{minute:02}:{second:02}"
        base = f"Asia/Jakarta-{date}-{time}"
        md5_hash = hashlib.md5(base.encode()).hexdigest()
        decrypted = ''.join([chr(b ^ ord(md5_hash[i])) for i, b in enumerate(flag)])

        if decrypted.isprintable() and decrypted.startswith("crYpt0"):
            print(f"[{time}] ➜ 1753c{{{decrypted}}}")
