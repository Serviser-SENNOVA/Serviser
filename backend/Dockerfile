FROM python:3.12
LABEL authors="Valwolfor"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "mi_aplicacion_serviser.wsgi:application", "--bind", "0.0.0.0:8000"]