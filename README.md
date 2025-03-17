# Digantara Backend Developer Assignment

## How to Build/Run the Solution

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd digantara
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

pip install -r requirements.txt
Apply migrations:

python manage.py makemigrations
python manage.py migrate
Run the server:

python manage.py runserver