Proyecto con modulos de trabajo. El primer modulo es sobre la incripción y diagnóstico de la empresa. 


mi_aplicacion_serviser/
│
├── backend/    # Todo lo relacionado a Django
│   ├── mi_app/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py    # Tus modelos Django aquí
│   │   ├── tests.py
│   │   └── views.py
│   │
│   ├── mi_aplicacion_serviser/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py   # Configuraciones de Django
│   │   ├── urls.py       # Rutas de tu aplicación Django
│   │   └── wsgi.py
│   │
│   ├── manage.py
│   ├── requirements.txt  # Dependencias de pip
│   └── Dockerfile        # Dockerfile para Django
│
├── frontend/   # Todo lo relacionado a React/TypeScript
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   ├── App.tsx
│   │   └── index.tsx
│   │
│   ├── package.json      # Dependencias de npm
│   ├── tsconfig.json     # Configuración de TypeScript
│   └── Dockerfile        # Dockerfile para React
│
└── docker-compose.yml    # Para orquestar los contenedores