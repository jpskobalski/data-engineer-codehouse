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