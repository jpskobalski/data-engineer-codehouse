Proyecto ETL Meteorológico con Airflow y Docker

Este proyecto consiste en un proceso ETL (Extracción, Transformación y Carga) que recolecta datos meteorológicos desde una API pública (OpenWeatherMap), los transforma y los carga en una base de datos Redshift. Además, se han implementado mecanismos de alertas meteorológicas configurables y flexibles. Todo el proyecto está dockerizado y se ejecuta dentro de un entorno de Apache Airflow.

Tabla de Contenidos

	• Descripción del Proyecto
	• Tecnologías Utilizadas
	• Estructura del Proyecto
	• Requisitos
	• Instalación y Configuración
	• Funcionamiento del DAG en Airflow
	• Mecanismo de Alerta
	• Modelado de la Tabla
	• Uso del Contenedor Docker

Descripción del Proyecto

Este sistema ETL automatizado permite la extracción diaria de datos meteorológicos para distintas ciudades, los cuales luego son procesados y almacenados en Amazon Redshift. A su vez, el sistema cuenta con un mecanismo de alertas flexibles, que permite definir límites personalizados para variables como la temperatura, la humedad y el viento.

El flujo de trabajo está completamente gestionado mediante Apache Airflow, permitiendo la planificación, monitorización y ejecución de cada paso del ETL. La aplicación ha sido dockerizada para asegurar que cualquier usuario pueda ejecutarla independientemente del sistema operativo.

Tecnologías Utilizadas

	• Python 3.9: Para el desarrollo del proceso ETL.
	• Apache Airflow: Para la gestión y planificación del flujo de trabajo.
	• Docker: Para la contenedorización de la aplicación.
	• Amazon Redshift: Como base de datos de destino para los datos meteorológicos.
	• SendGrid: Para el envío de alertas por email.
	• OpenWeatherMap API: Como fuente de datos meteorológicos.

Estructura del Proyecto
```bash
.
├── dags/
│   └── weather_etl_dag.py        # Definición del DAG de Airflow
├── scripts/
│   ├── main.py                   # Script principal que ejecuta el ETL
│   ├── extract.py                # Módulo de extracción de datos desde la API
│   ├── transform.py              # Módulo de transformación de los datos
│   ├── load.py                   # Módulo de carga de datos en Redshift
│   ├── config.py                 # Configuración (variables de entorno y API keys)
│   └── alert.py                  # Módulo de alertas meteorológicas
├── Dockerfile                    # Definición del contenedor Docker
├── requirements.txt              # Dependencias de Python
└── docker-compose.yml            # Orquestación de Docker
```
Requisitos

	• Docker y Docker Compose instalados en el sistema.
	• Cuenta en OpenWeatherMap para obtener una API key.
	• Base de datos Amazon Redshift configurada.
	• Cuenta en SendGrid para el envío de correos electrónicos de alerta.

Instalación y Configuración

	1. Clonar el repositorio:

```bash
git clone https://github.com/usuario/etl-weather-app.git
cd etl-weather-app
```
	2. Configurar las variables de entorno:
Crear un archivo .env con las siguientes variables (asegurarse de reemplazar los valores por los datos reales):

```bash
REDSHIFT_USER=tu_usuario_redshift
REDSHIFT_PASSWORD=tu_password_redshift
REDSHIFT_HOST=tu_host_redshift
REDSHIFT_PORT=5439
REDSHIFT_DATABASE=tu_base_de_datos_redshift

SENDGRID_API_KEY=tu_api_key_sendgrid
OPENWEATHER_API_KEY=tu_api_key_openweather
```

	3. Construir la imagen de Docker:
```bash
docker-compose build
```
 	4. Iniciar los servicios:
```bash
docker-compose up -d
```

	5. Acceder a Airflow:
Abrir un navegador web e ir a http://localhost:8080. Las credenciales predeterminadas son admin/admin.

Funcionamiento del DAG en Airflow

El DAG (Directed Acyclic Graph) está diseñado para ejecutarse diariamente y realizar las siguientes tareas:

	1. Extracción de datos: Se conecta a la API de OpenWeatherMap para obtener información meteorológica.
	2. Transformación de datos: Los datos extraídos son transformados a un formato adecuado para su posterior inserción en Redshift.
	3. Carga de datos: Los datos transformados son cargados en una tabla de Amazon Redshift.
	4. Envío de alertas: Si alguna de las ciudades monitoreadas excede los límites establecidos (temperatura, humedad, viento), se envía una alerta por correo electrónico utilizando el servicio de SendGrid.

Tareas del DAG:

	• run_etl: Ejecuta el flujo completo de extracción, transformación y carga.
	• send_alert: Envía alertas si se detectan condiciones climáticas que superan los umbrales definidos.

El DAG está configurado para admitir backfill, lo que significa que puede ejecutar tareas pasadas si es necesario.

Mecanismo de Alerta

El sistema de alertas permite configuraciones flexibles, como la modificación de los valores máximos y mínimos para las variables climáticas (temperatura, humedad, presión y velocidad del viento). El mensaje de alerta es completamente descriptivo y se puede personalizar según las necesidades del usuario. Los correos son enviados a través de la API de SendGrid.

Ejemplo de configuración de alerta:

```python
limites = {
    "temperatura": {"min": 0, "max": 35},
    "humedad": {"min": 30, "max": 70},
    "presion": {"min": 990, "max": 1020},
    "viento": {"max": 60}
}
send_alert(ciudad="Buenos Aires", temperatura=40, email="usuario@example.com", limites=limites)
```

Modelado de la Tabla

Antes de ejecutar el ETL, se debe crear la tabla en Redshift. A continuación se muestra el script SQL necesario para crear la tabla:

```sql
CREATE TABLE IF NOT EXISTS clima (
    ciudad VARCHAR(50),
    temperatura FLOAT,
    humedad INT,
    presion INT,
    viento FLOAT,
    descripcion VARCHAR(100),
    fecha TIMESTAMP,  
    fecha_extraccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    PRIMARY KEY (ciudad, fecha)
);
```

Esta tabla almacena los datos meteorológicos con claves primarias compuestas por ciudad y fecha.

Uso del Contenedor Docker

El contenedor Docker encapsula todo el entorno de ejecución del proyecto, asegurando que sea portable y fácil de ejecutar en cualquier máquina.

Comandos básicos:

	• Levantar el contenedor:
```bash
docker-compose up -d
```

	• Verificar el estado de los servicios:
```bash
docker-compose ps
```

	• Detener el contenedor:
```bash
docker-compose down
```
