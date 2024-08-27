FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

RUN pip install apache-airflow
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
RUN mkdir -p /opt/airflow/dags
COPY dags/weather_etl_dag.py /opt/airflow/dags/
COPY scripts /opt/airflow/scripts/

ENV AIRFLOW_HOME=/opt/airflow
WORKDIR $AIRFLOW_HOME

RUN airflow db init && \
    airflow users create \
    --username admin \
    --firstname Firstname \
    --lastname Lastname \
    --role Admin \
    --email admin@example.com \
    --password admin

CMD ["airflow", "webserver", "--port", "8080"]