# 🎮 GAMEHUB

**GAMEHUB** is a simple Django web application for browsing games, viewing details, reading and posting reviews, and managing content through an admin panel.

---

## 🛠️ Features

- 🗂️ List of games with images, genres, and descriptions  
- 🔍 Game detail pages  
- ✍️ Review system (read and post reviews)  
- ⚙️ Admin panel for managing games, reviews, and genres  

---

## 🚀 Tech Stack

- 💻 Python & Django  
- 🎨 HTML/CSS (Bootstrap or plain)  
- 🛢️ SQLite (default Django database)  

---

## 📦 Installation

```bash
git clone https://github.com/AmirAnsaripur/GAMEHUB.git
cd GAMEHUB

python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
