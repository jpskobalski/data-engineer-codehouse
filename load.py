import psycopg2
from config import REDSHIFT_USER, REDSHIFT_PASSWORD, REDSHIFT_HOST, REDSHIFT_PORT, REDSHIFT_DATABASE


def load_data(df):
    conn = psycopg2.connect(
        dbname=REDSHIFT_DATABASE,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT
    )
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS clima (
        ciudad VARCHAR(50),
        temperatura FLOAT,
        humedad INT,
        presion INT,
        viento FLOAT,
        descripcion VARCHAR(100),
        fecha TIMESTAMP
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO clima (ciudad, temperatura, humedad, presion, viento, descripcion, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row['ciudad'], row['temperatura'], row['humedad'], row['presion'], row['viento'], row['descripcion'],
             row['fecha'])
        )
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    from transform import transform_data
    from extract import extract_data

    data = extract_data()
    df = transform_data(data)
    load_data(df)