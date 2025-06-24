## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Authentication:** JWT-based authentication
- **Database:** PostgreSQL (or SQLite for dev)
- **Environment:** Python virtualenv + .env configs
- **Version Control:** Git + GitHub

## 📁 Project Structure
Pariyojana/
└── pariyojana_backend/
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    ├── .env
    ├── .gitignore

    ├── project_management/     # Django project root + global settings
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   ├── wsgi.py
    │   └── utils/
    │       └── helpers.py

    ├── common/                 # Shared base models, permissions, utils
    │   ├── models.py
    │   └── permissions.py

    ├── authentication/         # Your form letter authentication app
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── tests.py
    │   └── tokens.py

    ├── users/                  # User management (profiles, roles)
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   ├── urls.py
    │   └── permissions.py

    ├── user_auth/              # User login, JWT auth, logout
    │   ├── serializers.py
    │   ├── views.py
    │   ├── urls.py
    │   └── permissions.py

    ├── projects/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   ├── urls.py
    │   └── filters.py

    ├── inventory/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   └── urls.py

    ├── planning/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   └── urls.py

    ├── dashboard/
    │   ├── views.py
    │   └── urls.py

    ├── reports/
    │   ├── views.py
    │   ├── serializers.py
    │   └── urls.py

    ├── settings/
    │   ├── models.py
    │   ├── views.py
    │   └── urls.py

### 1. Clone the Repository

```bash
git clone https://github.com/Allan-Saud/pariyojana.git
cd pariyojana/pariyojana_backend

### 2. Create & Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

### 3. INstall Dependencies
pip install -r requirements.txt

### 4. Configure Environment Variables
Create a .env file in the root directory and set your environment variables:

SECRET_KEY=your_django_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password

### 5. Run Migrations
python manage.py makemigrations
python manage.py migrate

### 6. Start the Development Server
python manage.py runserver

