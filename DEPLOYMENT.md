# 🚀 Deployment Guide - Laptop Diagnosis Expert System

## 📋 Prerequisites
- GitHub account
- Vercel account (sign up with GitHub)
- Render account (sign up with GitHub)

---

## 🎯 Step-by-Step Deployment

### 1️⃣ **Push to GitHub** (if not already)
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

---

### 2️⃣ **Deploy Backend to Render**

1. Go to [render.com](https://render.com) and sign in
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name:** `laptop-diagnosis-api`
   - **Region:** Singapore (closest to Indonesia)
   - **Root Directory:** `backend`
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Instance Type:** Free
5. Add Environment Variable:
   - Key: `FLASK_ENV`, Value: `production`
6. Click **"Create Web Service"**
7. Wait 2-5 minutes for deployment
8. **Copy your backend URL** (e.g., `https://laptop-diagnosis-api.onrender.com`)

---

### 3️⃣ **Update Frontend Environment Variable**

Edit `frontend/.env.production`:
```env
VITE_API_URL=https://YOUR-BACKEND-URL.onrender.com/api
```
Replace `YOUR-BACKEND-URL` with the actual URL from Render.

Commit the change:
```bash
git add frontend/.env.production
git commit -m "Update production API URL"
git push
```

---

### 4️⃣ **Deploy Frontend to Vercel**

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Configure:
   - **Framework Preset:** Vite
   - **Root Directory:** `frontend`
   - **Build Command:** `npm run build` (auto-detected)
   - **Output Directory:** `dist` (auto-detected)
5. Click **"Deploy"**
6. Wait 1-2 minutes
7. Your site is live! 🎉

---

## 🔗 **URLs After Deployment**

- **Frontend:** `https://your-project.vercel.app`
- **Backend:** `https://laptop-diagnosis-api.onrender.com`

---

## ⚠️ **Important Notes**

### Render Free Tier:
- Backend will **sleep after 15 minutes** of inactivity
- First request after sleep takes ~30 seconds to wake up
- 750 hours/month free (enough for testing)

### To Keep Backend Always Active:
- Upgrade to paid plan ($7/month), OR
- Use a ping service like [UptimeRobot](https://uptimerobot.com) (free)

---

## 🧪 **Testing Your Deployment**

1. Open your Vercel frontend URL
2. First load might be slow (backend waking up)
3. Try diagnosis - should work!

---

## 🐛 **Troubleshooting**

### Frontend can't connect to backend:
- Check `.env.production` has correct backend URL
- Make sure URL ends with `/api`
- Check Render logs for backend errors

### Backend not starting:
- Check Render logs
- Verify `requirements.txt` is correct
- Check Python version compatibility

---

## 📞 **Need Help?**
Check logs:
- **Vercel:** Project → Deployments → Click deployment → Logs
- **Render:** Dashboard → Service → Logs tab

Good luck! 🚀
