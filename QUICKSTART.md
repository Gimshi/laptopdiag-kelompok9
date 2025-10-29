# 🚀 Quick Start Guide

## Langkah-langkah Setup Project

### 1. Install Dependencies

#### Backend
```powershell
cd backend
pip install -r requirements.txt
```

#### Frontend
```powershell
cd frontend
npm install
```

---

### 2. Jalankan Backend

```powershell
cd backend
python app.py
```

✅ Backend running di: **http://localhost:5000**

---

### 3. Jalankan Frontend

Buka terminal baru:

```powershell
cd frontend
npm run dev
```

✅ Frontend running di: **http://localhost:3000**

Browser akan terbuka otomatis!

---

### 4. Test di Browser

1. Pilih beberapa gejala kerusakan laptop
2. Klik tombol **"Diagnose"**
3. Lihat hasil diagnosis dengan solusi lengkap!

---

## 📓 Jupyter Notebook Demo

Untuk melihat cara kerja Forward Chaining secara detail:

```powershell
jupyter notebook forward_chaining_demo.ipynb
```

Atau buka file `.ipynb` langsung di VS Code dengan Jupyter extension.

---

## ✅ Checklist Testing

- [ ] Backend API berjalan di port 5000
- [ ] Frontend berjalan di port 3000
- [ ] Dapat load daftar symptoms
- [ ] Dapat pilih multiple symptoms
- [ ] Dapat klik "Diagnose" dan melihat hasil
- [ ] Results menampilkan diagnosis dengan solutions
- [ ] Jupyter notebook dapat dijalankan

---

## 🐛 Troubleshooting

### Port 5000 sudah dipakai?
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### CORS Error?
Pastikan backend running dan CORS sudah enabled (sudah di-setup).

### Frontend tidak bisa connect ke backend?
Cek `frontend/src/utils/api.js` - pastikan `API_BASE_URL` = `http://localhost:5000/api`

---

## 📚 Tech Stack Summary

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| AI Engine | Forward Chaining |
| Frontend | React + Vite |
| Styling | UnoCSS |
| Animation | Framer Motion |

---

**Happy Coding! 🎉**
