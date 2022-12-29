# learnify backend service

## Usage

### Clone project

📌 `git clone https://github.com/Yakser/learnify-backend.git`

### Create virtual environment

🔑 Copy `.env.example` to `.env` and change api settings

### Install dependencies

* 📎 Install dependencies with command `pip install -r requirements.txt`

### Apply migrations

🎓 Run  `python manage.py migrate`

### Run project

🚀 Run project via `python manage.py runserver`

## For developers

### Install pre-commit hooks

To install pre-commit simply run inside the shell:

```bash
pre-commit install
```

To run it on all of your files, do

```bash
pre-commit run --all-files
```
