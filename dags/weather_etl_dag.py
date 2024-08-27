from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.main import main

#argumentos
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

#DAG
with DAG(
        'weather_etl_dag',
        default_args=default_args,
        description='ETL para extraer, transformar y cargar datos meteorológicos de Buenos Aires en Redshift',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2024, 8, 27),
        catchup=False,
) as dag:
    # operador
    etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=main
    )

    etl_task