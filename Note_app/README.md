# 📝 Note App

A simple Note-taking web app built with **FastAPI**, **Jinja2 templates**, and **MySQL** — with a clean Notion-inspired dark UI.

---

## ✨ Features

- Add notes with a category (Work type), content, and date
- View all saved notes on the home page
- Delete notes with a single click
- Minimal, dark-themed UI built with plain HTML + CSS

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Database | MySQL (via `mysql-connector-python`) |
| Templating | Jinja2 |
| Frontend | HTML, CSS (custom Notion-style dark theme) |
| Server | Uvicorn |
| Config | `python-dotenv` |

---

## 📁 Project Structure

```
Note_app/
├── notes.py          # FastAPI app & all route handlers
├── database.py       # MySQL connection & DB/table setup
├── templates/
│   └── index.html    # Main UI template
├── static/
│   ├── style.css     # Dark theme stylesheet
│   ├── send.png      # Submit button icon
│   └── trash.png     # Delete button icon
├── .env              # Environment variables (not committed)
├── .env.example      # Example env file
└── requirements.txt
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.10+
- MySQL running locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/note-app.git
cd note-app
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=Notes
```

### 5. Set up the database

The app auto-creates the `Notes` database on startup. You just need to create the `User_record` table manually once:

```sql
CREATE DATABASE IF NOT EXISTS Notes;
USE Notes;

CREATE TABLE User_record (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    Work_type VARCHAR(50),
    Content   VARCHAR(200),
    Creation  DATE
);
```

### 6. Run the app

```bash
uvicorn notes:app --reload
```

Visit `http://localhost:8000` in your browser.

---

## 🗺️ Routes

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Redirects to `/home` |
| `GET` | `/home` | Displays all notes |
| `POST` | `/add` | Adds a new note |
| `POST` | `/delete/{note_id}` | Deletes a note by ID |

---

## 🖼️ UI Preview

The app uses a Notion-style dark theme with:
- A form at the top to add notes (category, date, content)
- Cards below listing all saved notes
- A trash icon button on each card to delete it

---

## 📦 Requirements

```
fastapi
uvicorn
jinja2
python-multipart
mysql-connector-python
python-dotenv
```

Generate `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## 🚧 Planned Improvements

- [ ] Edit existing notes
- [ ] Filter/search notes by category
- [ ] User authentication
- [ ] Migrate to SQLAlchemy ORM

---

## 📄 License

MIT
