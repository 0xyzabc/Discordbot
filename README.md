# Discord Auto-Messenger Bot 🤖

Bot otomatis untuk mengirim pesan ke channel Discord secara bergiliran dari beberapa akun.

## Fitur ✨
- Mengirim pesan dari multiple akun secara bergiliran
- Delay acak antara 5-10 detik antar akun
- Urutan pengiriman diacak setiap siklus
- Perlindungan dasar dengan memisahkan token ke file terpisah

## Prasyarat 📋
- Python 3.8+
- Akun Discord dengan token akses
- Akses ke channel Discord target

## Instalasi 🛠️

1. **Clone repositori**:
   ```bash
   git clone https://github.com/0xyzabc/Discordbot.git
   cd Discordbot

2. **Buat file konfigurasi**:
   Buat file tokens.py dan isi dengan:
    USER_TOKENS = [
    "token_akun_1",
    "token_akun_2",
    "token_akun_3"
]

3.  **Install dependencies**:
    CHANNEL_ID = '123456789012345678'

## Jalankan bot dengan
  python3 main.py

##  Struktur File 📂
  bot-discord/
├── main.py            # Skrip utama bot
├── tokens.py          # File penyimpanan token (gitignore)
├── README.md          # Dokumentasi ini
└── .gitignore         # File ignore untuk token