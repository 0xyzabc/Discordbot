# main.py - File utama bot Discord
import time
import requests
import random
from tokens import USER_TOKENS  # Import token dari file terpisah

# Daftar pesan khusus tiap akun
USER_MESSAGES = [
    "Halo, saya User 1 hadir!",
    "User 2 di sini, semangat ya!",
    "User 3 checking in, yuk lanjut!"
]

CHANNEL_ID = '892970303137939480'  # Ganti dengan channel ID tujuan

HEADERS_TEMPLATE = {
    'accept': '*/*',
    'content-type': 'application/json',
    'origin': 'https://discord.com',
    'referer': f'https://discord.com/channels/{CHANNEL_ID}',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
}

def send_message(token, message):
    url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'
    headers = HEADERS_TEMPLATE.copy()
    headers['authorization'] = token
    data = {"content": message, "tts": False}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"[+] Pesan terkirim dari akun: {token[:15]}... ✓")
        else:
            print(f"[x] Gagal kirim pesan dari akun: {token[:15]}... ✗", response.status_code)
    except Exception as e:
        print(f"[!] Error: {e}")

def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"[⏳] Menunggu {remaining} detik...", end="\r")
        time.sleep(1)
    print("[✓] Lanjut ke akun berikutnya!")

def main():
    while True:
        # Gabung token dan pesan lalu acak urutan
        user_data = list(zip(USER_TOKENS, USER_MESSAGES))
        random.shuffle(user_data)

        # Cek urutan pengiriman kali ini
        print("🔀 Urutan pengiriman kali ini:")
        for idx, (token, message) in enumerate(user_data, 1):
            print(f"{idx}. Akun: {token[:12]}... | Pesan: {message}")

        # Kirim pesan sesuai urutan yang diacak
        for token, message in user_data:
            send_message(token, message)
            delay = random.randint(5, 10)
            countdown_timer(delay)

        print("[🚀] Selesai kirim semua, tunggu 60 detik...")
        countdown_timer(60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[!] Program dihentikan.")