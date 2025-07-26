CREATE DATABASE bd_peliculas;

USE bd_peliculas;

CREATE TABLE peliculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(100),
    clasificacion VARCHAR(100),
    genero VARCHAR(100),
    idioma VARCHAR(100)
);