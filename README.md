# 🌱 Penghijauan GitHub

Automasi untuk menjaga kontribusi GitHub tetap hijau setiap hari! 🚀

## 📋 Deskripsi

Repository ini menggunakan GitHub Actions untuk membuat commit otomatis setiap hari, sehingga contribution graph GitHub Anda tetap hijau dan streak tetap terjaga.

## ✨ Fitur

- ✅ **Auto Commit Harian** - Commit otomatis setiap hari jam 10:00 WIB
- ⏰ **Jadwal Fleksibel** - Bisa diatur sesuai kebutuhan
- 🤖 **Fully Automated** - Tidak perlu intervensi manual
- 📊 **Activity Log** - Menyimpan riwayat semua aktivitas

## 🚀 Cara Menggunakan

### 1. Fork atau Clone Repository Ini

```bash
git clone https://github.com/faiisallmn/penghijauan.git
cd penghijauan
```

### 2. Aktifkan GitHub Actions

- Buka repository di GitHub
- Pergi ke tab **Actions**
- Klik **"I understand my workflows, go ahead and enable them"**

### 3. Biarkan Berjalan Otomatis! 🎉

GitHub Actions akan otomatis menjalankan commit setiap hari jam 10:00 WIB.

## 🔧 Konfigurasi

### Mengubah Jadwal

Edit file `.github/workflows/auto-commit.yml` dan ubah bagian `cron`:

```yaml
schedule:
  # Format: menit jam hari bulan hari_minggu
  - cron: '0 3 * * *'  # 10:00 WIB = 03:00 UTC
```

**Contoh Jadwal:**
- `'0 0 * * *'` - Setiap hari jam 07:00 WIB
- `'0 6 * * *'` - Setiap hari jam 13:00 WIB
- `'0 12 * * *'` - Setiap hari jam 19:00 WIB

### Menjalankan Manual

1. Buka tab **Actions** di GitHub
2. Pilih workflow **"Daily Auto Commit"**
3. Klik **"Run workflow"**

## 📁 Struktur File

```
penghijauan/
├── .github/
│   └── workflows/
│       └── auto-commit.yml    # GitHub Actions workflow
├── auto_commit.py             # Script Python untuk auto commit
├── activity.log               # Log aktivitas harian
└── README.md                  # Dokumentasi ini
```

## 🛠️ Teknologi

- **GitHub Actions** - Automasi workflow
- **Python 3.x** - Script untuk update log
- **Git** - Version control

## ⚠️ Catatan Penting

- Repository ini **harus publik** atau Anda perlu GitHub Pro untuk GitHub Actions di private repo
- Pastikan **GitHub Actions** sudah diaktifkan di repository settings
- Workflow akan berjalan otomatis setelah push pertama

## 📊 Monitoring

Anda bisa melihat riwayat eksekusi workflow di:
- Tab **Actions** di repository GitHub
- File `activity.log` untuk melihat log aktivitas

## 🤝 Kontribusi

Jika Anda memiliki ide untuk improvement:
1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/improvement`)
3. Commit perubahan (`git commit -m 'Add some improvement'`)
4. Push ke branch (`git push origin feature/improvement`)
5. Buat Pull Request

## 📄 Lisensi

Free to use! Silakan fork dan modifikasi sesuai kebutuhan Anda.

## 🌟 Tips

- Kombinasikan dengan kontribusi asli untuk hasil terbaik
- Jangan terlalu bergantung pada automasi, tetap berkontribusi secara nyata!
- Sesuaikan jadwal agar terlihat natural

---

**Happy Coding! 💻✨**

Dibuat dengan ❤️ untuk menjaga GitHub tetap hijau 🌱
