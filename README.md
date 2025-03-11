
## 📜 **Project Overview**

- **User Authentication (Signup & Login)**
- **Create, Update, and Retrieve Notes**
- **MongoDB Atlas Integration**
- **Django REST Framework (DRF) APIs**

---

## 🛠️ **Requirements**

Ensure you have the following installed:

- **Python** (3.11+)
- **MongoDB Atlas Account**
- **Virtual Environment (venv)**

---

## ⚙️ **Installation & Setup**

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/ARUN-AK5011/NoteServer.git
cd notes-app/server
```

### 2️⃣ Create a Virtual Environment

```sh
python -m venv venv
```

#### In Windows

```sh
venv\Scripts\activate
```

#### In Linux

```sh
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 5️⃣ Run Database Migrations

```sh
python manage.py makemigrations notes
python manage.py migrate
```

### 6️⃣ Start the Django Server

```sh
python manage.py runserver
```
