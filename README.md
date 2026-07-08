# AirAsia Project

An automation project by **GladexAutomate**.

## What is this?

This project has two parts:

1. **The website** (`index.html`) — the public Gladex Travel & Tours site,
   deployed automatically to **Vercel** every time you push to GitHub.
2. **Optional automation scripts** (`src/` folder) — Python code for behind-the-
   scenes tasks. These are **not** part of the website (Vercel ignores them via
   `.vercelignore`).

To change the website, edit `index.html`, then commit and push — Vercel
redeploys it live in a few seconds.

## Folder structure

```
Airasia-Project/
├── README.md            <- You are here (project overview)
├── requirements.txt     <- List of Python packages the project needs
├── .env.example         <- Template for secret settings (passwords, API keys)
├── .gitignore           <- Files git should ignore (secrets, logs, etc.)
├── src/                 <- Your main code lives here
│   ├── main.py          <- The starting point — run this file
│   └── utils/
│       └── helpers.py   <- Reusable helper functions (logging, etc.)
├── data/                <- Input/output data files (CSV, JSON, etc.)
├── logs/                <- Log files are written here automatically
└── tests/               <- Tests to check your code works
    └── test_main.py
```

## How to get started (step by step)

1. **Install Python** (version 3.10 or newer) from https://python.org
2. **Open a terminal** in this folder.
3. **(Optional) Create a virtual environment** so packages stay tidy:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   ```
4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Copy the settings template** and fill in your own values:
   ```bash
   copy .env.example .env       # Windows
   ```
6. **Run the project:**
   ```bash
   python src/main.py
   ```

## Saving your work to GitHub

Whenever you want to save your changes online:

```bash
git add .
git commit -m "Describe what you changed"
git push
```

---
Repository: https://github.com/GladexAutomate/Airasia-Project
