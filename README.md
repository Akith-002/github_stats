# 🚀 GitHub Profile Statistics

An interactive web app that retrieves and displays GitHub user statistics using **Flask** for the backend and **Streamlit** for the frontend.

## 📌 Features
- Fetches GitHub user details like name, bio, followers, and repositories.
- Simple and user-friendly **Streamlit** UI.
- Uses the **GitHub API** to get real-time data.
- Built with **Flask (backend)** and **Streamlit (frontend)**.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Akith-002/github_stats.git
cd github_stats
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Backend (Flask API)
```bash
python app.py
```
The Flask server will start at `http://127.0.0.1:5000/`

### 4️⃣ Run the Frontend (Streamlit UI)
```bash
python -m streamlit run frontend.py
```

---

## 📡 API Endpoint
The backend exposes an API endpoint to fetch GitHub user statistics:
```http
GET /github-stats?username=<github_username>
```
### Example Request
```bash
curl http://127.0.0.1:5000/github-stats?username=octocat
```
### Example Response
```json
{
  "name": "The Octocat",
  "avatar_url": "https://github.com/images/error/octocat_happy.gif",
  "public_repos": 8,
  "followers": 3938,
  "following": 9,
  "bio": "GitHub mascot",
  "location": "San Francisco"
}
```

---

## 🤝 Contributing
Feel free to **fork** this repository and contribute! 🚀

1. Fork the project
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---

## 🛠 Built With
- **Python** 🐍
- **Flask** (Backend API) 🔥
- **Streamlit** (Frontend UI) 🎨
- **GitHub API** 🐙

---

## 📬 Contact
- **GitHub**: [Akith-002](https://github.com/Akith-002)
- **Email**: akith.chandinu@gmail.com

---

Give this project a ⭐ if you found it helpful! 🚀
