Smart Canteen - Django + MySQL backend
-------------------------------------
Setup:
1. Create a Python virtualenv and activate it.
2. pip install -r requirements.txt
3. Edit backend/smartcanteen/settings.py DATABASES with your MySQL credentials.
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver
Seed data:
- Run: python manage.py shell
- Then: exec(open('api/seed_data.py').read())
