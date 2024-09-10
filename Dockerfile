FROM python:3.9-slim

# Instalar solo lo necesario
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Instalar Airflow y otras dependencias
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Configurar Airflow
RUN mkdir -p /opt/airflow/dags
COPY dags/ /opt/airflow/dags/
COPY scripts/ /opt/airflow/scripts/

ENV AIRFLOW_HOME=/opt/airflow
WORKDIR $AIRFLOW_HOME

# Inicializar Airflow
RUN airflow db init

CMD ["airflow", "webserver", "--port", "8080"]