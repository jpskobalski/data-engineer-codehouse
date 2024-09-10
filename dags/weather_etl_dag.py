from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.main import main
from scripts.alert import send_alert

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'weather_etl_dag',
    default_args=default_args,
    description='ETL para extraer, transformar y cargar datos meteorológicos en Redshift',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 8, 27),
    catchup=True,  # Activar backfill
) as dag:

    # Tarea para ejecutar el script ETL
    etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=main
    )

    # Tarea para enviar alertas
    send_alert_task = PythonOperator(
        task_id='send_alert',
        python_callable=send_alert,
        op_args=["ciudad", 20, 50, 1000, 30, "clear sky", "test@example.com"],  # Puedes ajustar esto según sea necesario
    )

    etl_task >> send_alert_task