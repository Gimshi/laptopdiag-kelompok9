# 🚀 Quick Deployment Guide

## Files Created:
✅ `backend/app.py` - Updated for production
✅ `backend/render.yaml` - Render config
✅ `frontend/.env.production` - Production API URL
✅ `frontend/.env.development` - Development API URL
✅ `frontend/vercel.json` - Vercel config
✅ `frontend/src/utils/api.js` - Updated to use env variables

---

## 🎯 Deploy in 3 Steps:

### 1. Deploy Backend to Render
1. Go to render.com → New Web Service
2. Connect GitHub repo
3. Settings:
   - Root Directory: `backend`
   - Build: `pip install -r requirements.txt`
   - Start: `python app.py`
4. Copy your URL (e.g., https://xxx.onrender.com)

### 2. Update Frontend API URL
Edit `frontend/.env.production`:
```
VITE_API_URL=https://YOUR-RENDER-URL.onrender.com/api
```

### 3. Deploy Frontend to Vercel
1. Go to vercel.com → New Project
2. Import GitHub repo
3. Settings:
   - Root Directory: `frontend`
   - Framework: Vite (auto-detected)
4. Deploy!

---

## ⚠️ Note:
- Render free tier sleeps after 15 min idle
- First request takes ~30s to wake up
- Vercel is always fast!

Done! 🎉
