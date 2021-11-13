cd /root/server
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8080
