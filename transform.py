import pandas as pd

def transform_data(data):
    df = pd.DataFrame([{
        'ciudad': data['name'],
        'temperatura': data['main']['temp'],
        'humedad': data['main']['humidity'],
        'presion': data['main']['pressure'],
        'viento': data['wind']['speed'],
        'descripcion': data['weather'][0]['description'],
        'fecha': pd.to_datetime(data['dt'], unit='s')
    }])

    # Limpiar duplicados basados en ciudad y fecha
    df.drop_duplicates(subset=['ciudad', 'fecha'], keep='last', inplace=True)

    # Reemplazar valores nulos con default values
    df['temperatura'].fillna(df['temperatura'].mean(), inplace=True)
    df['humedad'].fillna(df['humedad'].mean(), inplace=True)
    df['presion'].fillna(df['presion'].mean(), inplace=True)
    df['viento'].fillna(df['viento'].mean(), inplace=True)
    df['descripcion'].fillna("Sin descripción", inplace=True)

    return df

if __name__ == "__main__":
    from extract import extract_data
    data = extract_data()
    df = transform_data(data)
    print(df.head())