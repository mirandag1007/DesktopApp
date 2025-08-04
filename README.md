# DesktopApp
## SWE Desktop App 

## Features
- Note-taking requests
- Accept and fulfill requests from other students
- Secure login and user authentication

## Using
- Language: Python 3.x
- GUI Framework: Tkinter
- Database: SQLite 
- Version Control: Git + GitHub
  

## Desktop App Layout

<pre>
SWE-project-root/
│
├── app/                        ← Main application logic (like Next.js app folder)
│   ├── main.py                 ← Entry point for the app (equivalent to `page.tsx`)
│   ├── database.py               ← Handles Database
│
├── screens/                    ← Each window/screen in the app (like routes)
│   ├── dashboard.py            ← Dashboard view after login
│   ├── login.py                ← Login/Signup screen
│   └── post_request.py         ← Form for submitting a request
│
├── assets/                     ← Static files like images/icons (replaces `public/`)
│   ├── logo.png
│   └── background.jpg
├── requirements.txt            ← Python dependencies
├── README.md                   ← Project documentation
└── .gitignore                  ← Git exclusions (e.g., *.db, __pycache__)
</pre>







