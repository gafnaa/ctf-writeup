import nclib
import numpy as np

def min_path_sum(grid, rows, cols):
    """Menggunakan DP untuk mencari minimum path sum dalam grid."""
    dp = np.zeros((rows, cols), dtype=int)

    # Inisialisasi nilai awal
    dp[0][0] = grid[0][0]

    # Isi baris pertama (hanya bisa dari kiri)
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Isi kolom pertama (hanya bisa dari atas)
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Isi sisanya (minimalkan sum)
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]  # Jawaban ada di kanan bawah

def main():
    server = ('94.237.62.255', 30978)
    nc = nclib.Netcat(connect=server)
    nc.settimeout(None)

    while True:
        # Terima data dari server
        message = nc.recv().decode().strip()
        print("Received:", message)

        # Filter hanya baris yang berisi angka, hindari baris kosong
        numeric_lines = [line for line in message.split("\n") if line and line[0].isdigit()]

        if len(numeric_lines) < 2:
            continue  # Tunggu sampai input yang valid diterima

        # Ambil ukuran grid
        rows, cols = map(int, numeric_lines[0].split())

        # Ambil angka dalam grid
        numbers = list(map(int, " ".join(numeric_lines[1:]).split()))
        grid = [numbers[i * cols:(i + 1) * cols] for i in range(rows)]

        # Hitung minimum path sum
        result = min_path_sum(grid, rows, cols)
        print(f"Sending: {result}")

        # Kirim hasil ke server
        nc.send(f"{result}\n".encode())

if __name__ == '__main__':
    main()
