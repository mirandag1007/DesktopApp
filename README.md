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
- To run: please install first:
   pip install ttkbootstrap
  Then: python main.py 

  

## Desktop App Layout

# Project Structure

```text
SWE-project-root/
│
├── app/                        
│   ├── main.py                 ← Entry point for the app (equivalent to `page.tsx`)
│   ├── database.py             ← Handles Database
│
├── screens/                    
│   ├── dashboard.py            ← Dashboard view after login
│   ├── login.py                ← Login/Signup screen
│   └── post_request.py         ← Form for submitting a request
│
├── assets/                     
│   ├── logo.png
│   └── background.jpg
│
├── requirements.txt            ← Python dependencies
├── README.md                   ← Project documentation
└── .gitignore                  ← Git exclusions (e.g., *.db, __pycache__)
