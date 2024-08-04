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
    return df

if __name__ == "__main__":
    from extract import extract_data
    data = extract_data()
    df = transform_data(data)
    print(df.head())