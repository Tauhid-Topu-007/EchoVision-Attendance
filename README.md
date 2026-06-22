# 📸 EchoVision - AI-Powered Smart Attendance System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-2.0+-green.svg)](https://supabase.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**EchoVision** is an intelligent attendance management system that leverages cutting-edge AI technologies including **face recognition** and **voice biometrics** to automate classroom attendance tracking. Built with Streamlit and Supabase, it provides a seamless experience for both teachers and students.

---

## 🌟 Live Demo

🔗 **Try EchoVision Now:** [https://7yvdehgggjxxrxt55lgpqd.streamlit.app/](https://7yvdehgggjxxrxt55lgpqd.streamlit.app/)

---

## ✨ Features

### 🎯 Core Features
- **Face Recognition Attendance**: 98% accuracy using dlib's 128-d embeddings
- **Voice Biometrics**: Alternative attendance via Resemblyzer speaker verification
- **Dual-Portal System**: Separate dashboards for teachers and students
- **Real-time Analytics**: Live attendance tracking and reports
- **QR Code Enrollment**: Instant subject joining via QR codes
- **Multi-Photo Processing**: Batch process multiple classroom images

### 👨‍🏫 Teacher Features
- Create and manage subjects with unique codes
- Take AI-powered attendance (face + voice)
- View attendance records and analytics
- Share subject codes and QR links
- Track student statistics

### 👨‍🎓 Student Features
- Face recognition login
- Enroll in subjects via QR codes
- View personal attendance history
- Track subject-wise attendance
- Voice profile registration

---

## 📊 Impact

| Metric | Traditional | EchoVision |
|--------|-------------|------------|
| ⏰ Time per class | 10-15 mins | 2 seconds |
| 📊 Accuracy | ~85% | 98% |
| 📝 Paper usage | High | Zero |
| 🔒 Proxy attendance | Possible | Eliminated |
| 📈 Analytics | Manual | Real-time |

---

## 🏗️ Architecture
┌─────────────────────────────────────┐
│ Streamlit Frontend │
│ (Teacher & Student Dashboards) │
└────────────────┬────────────────────┘
│
┌────────────────▼────────────────────┐
│ Python Business Logic │
│ - Face Recognition Pipeline │
│ - Voice Biometrics Pipeline │
│ - Database Operations │
└────────────────┬────────────────────┘
│
┌────────────────▼────────────────────┐
│ AI/ML Processing Layer │
│ - dlib (128-d embeddings) │
│ - Resemblyzer (512-d voice emb) │
│ - Scikit-learn SVC Classifier │
└────────────────┬────────────────────┘
│
┌────────────────▼────────────────────┘
│ Supabase Database Layer │
│ - PostgreSQL with RLS │
│ - Real-time subscriptions │
│ - Secure authentication │
└─────────────────────────────────────┘


---

## 💻 Technology Stack

### Frontend
- **Streamlit** - Interactive web application framework (1.28+)
- **HTML/CSS** - Custom styling and responsive design
- **JavaScript** - Client-side interactions
- **Plotly** - Interactive data visualization (5.17+)
- **Pandas** - Data manipulation and display (2.0+)

### Backend & Database
- **Python** - Core programming language (3.8+)
- **Supabase** - Backend-as-a-Service with PostgreSQL (2.0+)
- **PostgreSQL** - Relational database with Row Level Security (15+)
- **bcrypt** - Password hashing and security (4.0+)

### AI & Machine Learning
- **dlib** - Face detection and 128-dimensional embeddings (19.24+)
- **OpenCV** - Image processing and computer vision (4.8+)
- **face_recognition** - Face recognition utilities (1.3+)
- **Resemblyzer** - Speaker verification and voice embeddings (0.1+)
- **Librosa** - Audio processing and feature extraction (0.10+)
- **Scikit-learn** - SVM classifier for recognition (1.3+)
- **NumPy** - Numerical computations (1.24+)
- **SciPy** - Scientific computing (1.10+)

### Development & Deployment
- **Git** - Version control
- **GitHub** - Source code hosting
- **Streamlit Cloud** - Application deployment
- **python-dotenv** - Environment variable management (1.0+)
- **Pillow** - Image processing and manipulation (10.0+)

---

## 📁 Project Structure
echovision-attendance/
├── app.py # Main application entry
├── requirements.txt # Python dependencies
├── .env.example # Environment variables template
├── .gitignore # Git ignore rules
│
├── src/
│ ├── screens/ # Page components
│ │ ├── home_screen.py
│ │ ├── teacher_screen.py
│ │ └── student_screen.py
│ │
│ ├── components/ # Reusable components
│ │ ├── header.py
│ │ ├── footer.py
│ │ ├── subject_card.py
│ │ └── dialog_*.py # Dialog components
│ │
│ ├── database/ # Database operations
│ │ ├── config.py
│ │ └── db.py
│ │
│ ├── pipelines/ # AI pipelines
│ │ ├── face_pipeline.py
│ │ └── voice_pipeline.py
│ │
│ └── ui/ # UI styling
│ └── base_layout.py
│
├── tests/ # Unit tests
│ ├── test_db.py
│ └── test_pipelines.py
│
└── docs/ # Documentation
├── api.md
├── deployment.md
└── contributing.md


---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Supabase account
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Tauhid-Topu-007/EchoVision-Attendance.git
cd EchoVision-Attendance

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your Supabase credentials

# Run the application
streamlit run app.py ```
