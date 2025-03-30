import nclib
import time

def createResponse(message):
    words = message.replace(',', '').split()  # Hapus koma dan pecah menjadi kata-kata
    challenge = []

    for word in words:
        if word == 'GORGE':
            challenge.append('STOP')
        elif word == 'PHREAK':
            challenge.append('DROP')
        elif word == 'FIRE':
            challenge.append('ROLL')

    answer = '-'.join(challenge)  # Gabungkan dengan format yang diharapkan
    answer = answer.strip() + '\n'  # Pastikan hanya ada satu newline di akhir
    print(answer)  # Debugging output
    return answer

def main():
    server = ('94.237.63.32', 55143)
    nc = nclib.Netcat(connect=server)
    nc.settimeout(10)

    # Terima pesan awal
    intro = nc.recv().decode()
    print("Received:", intro)

    if "Are you ready?" in intro:
        nc.send(b'y\n')

    while True:
        try:
            message = nc.recv().decode().strip()
            if not message:
                print("Connection closed by server.")
                break

            print("Received:", message)

            if "what do you do?" in message:
                challenge_text = message.split("What do you do?")[0].strip()
                answer = createResponse(challenge_text)

                # Debugging sebelum pengiriman
                print(f"Sending: {answer.encode()}")

                # Kirim jawaban
                nc.send(answer.encode())  

                # Kurangi delay agar tidak kehabisan waktu
                time.sleep(0.5)

        except Exception as e:
            print("Error:", e)
            break

if __name__ == '__main__':
    main()

