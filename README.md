# 🤖 Laptop Diagnosis Expert System

test

Sistem Pakar untuk mendeteksi kerusakan laptop menggunakan **Forward Chaining AI Algorithm**.

![Tech Stack](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![React](https://img.shields.io/badge/React-18.3-cyan)
![Vite](https://img.shields.io/badge/Vite-5.1-purple)
![UnoCSS](https://img.shields.io/badge/UnoCSS-0.58-orange)

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Forward Chaining Algorithm](#forward-chaining-algorithm)
- [Screenshots](#screenshots)

## ✨ Features

### Backend (AI Engine)
- ✅ **Forward Chaining Inference Engine** - Data-driven reasoning
- ✅ **Knowledge Base** - 20 symptoms & 15 diagnosis rules
- ✅ **REST API** - Flask dengan CORS support
- ✅ **Detailed Trace** - Step-by-step reasoning explanation
- ✅ **Confidence Scoring** - Akurasi diagnosis

### Frontend (UI/UX)
- ✅ **Modern UI** - React + UnoCSS (Tailwind-like utilities)
- ✅ **Smooth Animations** - Framer Motion
- ✅ **Responsive Design** - Mobile-friendly
- ✅ **Interactive Forms** - Multi-select symptoms
- ✅ **Beautiful Results** - Color-coded severity & solutions

### Jupyter Notebook
- ✅ **Step-by-Step Demo** - Forward chaining demonstration
- ✅ **Multiple Scenarios** - Test cases
- ✅ **Algorithm Deep Dive** - Internal trace visualization

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming language |
| Flask | Web framework & REST API |
| Flask-CORS | Cross-origin resource sharing |

### Frontend
| Technology | Purpose |
|------------|---------|
| React 18 | UI library |
| Vite | Build tool & dev server |
| UnoCSS | Utility-first CSS framework |
| Framer Motion | Animation library |
| Axios | HTTP client |
| Lucide React | Icon library |

## 📁 Project Structure

```
detect-kerusakan-laptop/
├── backend/
│   ├── app.py                  # Flask REST API
│   ├── forward_chaining.py     # AI inference engine
│   ├── knowledge_base.py       # Rules & symptoms
│   └── requirements.txt        # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── SymptomSelector.jsx
│   │   │   ├── DiagnosisResults.jsx
│   │   │   └── LoadingSpinner.jsx
│   │   ├── utils/
│   │   │   └── api.js          # API service
│   │   ├── App.jsx             # Main app
│   │   └── main.jsx            # Entry point
│   ├── package.json
│   ├── vite.config.js
│   ├── uno.config.js           # UnoCSS config
│   └── index.html
│
├── forward_chaining_demo.ipynb # Jupyter notebook demo
└── README.md
```

## 🚀 Installation

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm or yarn

### Backend Setup

1. Navigate to backend directory:
```powershell
cd backend
```

2. Create virtual environment (recommended):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

### Frontend Setup

1. Navigate to frontend directory:
```powershell
cd frontend
```

2. Install dependencies:
```powershell
npm install
```

## 🎮 Usage

### Running the Backend

```powershell
cd backend
python app.py
```

Backend akan berjalan di: **http://localhost:5000**

Output:
```
============================================================
🚀 Laptop Diagnosis Expert System API
============================================================
📍 Running on: http://localhost:5000
📖 API Docs: http://localhost:5000/

🔧 Available endpoints:
   GET  /api/symptoms  - Get all symptoms
   POST /api/diagnose  - Diagnose laptop issues
   GET  /api/rules     - Get all rules
   GET  /api/health    - Health check
============================================================
```

### Running the Frontend

```powershell
cd frontend
npm run dev
```

Frontend akan berjalan di: **http://localhost:3000**

Browser akan terbuka otomatis!

### Running Jupyter Notebook

```powershell
jupyter notebook forward_chaining_demo.ipynb
```

Atau buka di VS Code dengan Jupyter extension.

## 📡 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Get All Symptoms
```http
GET /api/symptoms
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "code": "S01",
      "description": "Laptop tidak bisa menyala sama sekali"
    },
    ...
  ],
  "total": 20
}
```

#### 2. Diagnose
```http
POST /api/diagnose
Content-Type: application/json

{
  "symptoms": ["S05", "S06", "S19"],
  "detailed": true
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "symptoms_provided": [...],
    "diagnoses_found": [
      {
        "rule_id": "R04",
        "diagnosis": "Overheating - Sistem Pendingin Bermasalah",
        "category": "hardware",
        "severity": "sedang",
        "confidence": 100.0,
        "description": "...",
        "solutions": [...]
      }
    ],
    "reasoning_steps": [...],
    "summary": {
      "total_symptoms": 3,
      "total_diagnoses": 1,
      "rules_fired": 1,
      "iterations": 2
    }
  }
}
```

#### 3. Get All Rules
```http
GET /api/rules
```

#### 4. Health Check
```http
GET /api/health
```

## 🧠 Forward Chaining Algorithm

### Konsep

Forward Chaining adalah metode inferensi **data-driven** (bottom-up reasoning):

```
Fakta (Symptoms) → Rules Matching → Conclusion (Diagnosis)
```

### Algoritma

```python
def forward_chaining(symptoms):
    working_memory = set(symptoms)
    fired_rules = []
    inferred_facts = []
    
    while True:
        rule_fired = False
        
        for rule in knowledge_base.rules:
            if rule not in fired_rules:
                if all(condition in working_memory for condition in rule.conditions):
                    # Fire rule
                    working_memory.add(rule.conclusion)
                    fired_rules.append(rule)
                    inferred_facts.append(rule.conclusion)
                    rule_fired = True
        
        if not rule_fired:
            break  # No more rules can fire
    
    return inferred_facts
```

### Example Trace

**Input:** `['S05', 'S06', 'S19']` (Laptop panas, kipas keras, mati sendiri)

**Process:**
```
Step 1: Initialize working memory with symptoms
  Working Memory: {S05, S06, S19}

Step 2: Check all rules
  Rule R04 matches: IF S05 AND S06 AND S19 THEN Overheating

Step 3: Fire Rule R04
  Conclusion: Overheating - Sistem Pendingin Bermasalah
  
Step 4: No more rules to fire
  DONE
```

**Output:** Diagnosis "Overheating" dengan confidence 100%

### Knowledge Base

#### Symptoms (20 total)
- S01-S20: Berbagai gejala kerusakan laptop
- Contoh: S01 (Tidak bisa nyala), S05 (Overheat), S15 (BSOD)

#### Rules (15 total)
- R01-R15: Aturan diagnosis
- Format: `IF symptom_codes THEN diagnosis`
- Contoh:
  ```
  R04: IF S05 AND S06 AND S19 
       THEN Overheating - Sistem Pendingin Bermasalah
  ```

## 🎨 Screenshots

### Home Page
Beautiful gradient background dengan modern UI.

### Symptom Selection
Multi-select cards dengan smooth animations.

### Diagnosis Results
Color-coded severity (Ringan/Sedang/Berat) dengan detailed solutions.

## 🧪 Testing

### Test Scenarios (Jupyter Notebook)

1. **Scenario 1: Overheat**
   - Symptoms: S05, S06, S19
   - Expected: Overheating diagnosis

2. **Scenario 2: Won't Turn On**
   - Symptoms: S01, S08
   - Expected: Charger/Port charging issue

3. **Scenario 3: Software Issue**
   - Symptoms: S03, S15, S04
   - Expected: Driver/OS corruption

4. **Scenario 4: Multiple Issues**
   - Symptoms: S03, S16, S20, S17
   - Expected: Multiple diagnoses (RAM + HDD)

## 📝 Development

### Add New Symptom

Edit `backend/knowledge_base.py`:
```python
def _initialize_symptoms(self):
    return {
        'S01': 'Description...',
        'S21': 'Your new symptom',  # Add here
    }
```

### Add New Rule

Edit `backend/knowledge_base.py`:
```python
def _initialize_rules(self):
    return {
        'R16': {  # Add new rule
            'conditions': ['S21', 'S22'],
            'conclusion': {
                'diagnosis': 'New Diagnosis',
                'category': 'hardware',
                'severity': 'sedang',
                'solutions': ['Solution 1', 'Solution 2'],
                'description': 'Description...'
            }
        }
    }
```

## 🐛 Troubleshooting

### Backend not starting?
```powershell
# Check if port 5000 is available
netstat -ano | findstr :5000

# Kill process if needed
taskkill /PID <PID> /F
```

### Frontend CORS error?
Make sure backend is running on `http://localhost:5000`

### Symptoms not loading?
Check browser console for errors. Verify backend API is accessible.

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📄 License

MIT License - feel free to use for educational purposes.

## 👨‍💻 Author

Created for **Pengantar Kecerdasan Buatan** course at UNJ.

---

**🚀 Happy Diagnosing! 🔧**
