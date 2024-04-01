# Corre la app en local

Primero crea un entorno virtual con python para evitar conflicto de versione

```bash
python -m venv venv-servicer
source venv-servicer/bin/activate  # En Windows usa `venv\Scripts\activate`
```
Instala las dependencias de Django y guircorn(servidor).

```bash
pip install django djangorestframework gunicorn
```

Facilitar la conexión a backend
```bash
pip install django-cors-headers
```

TO DOCKER
```bash
python manage.py makemigrations 
python manage.py migrate        
```

python manage.py createsuperuser [valwolfor : serviser2024*]

python manage.py runserver