-- SE CREA BASE DE DATOS
create database prueba_tecnica;

-- SE CREA TABLA DE LIBROS
CREATE TABLE libros (
    lib_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    lib_nombre VARCHAR(150) NOT NULL,
    lib_descripcion VARCHAR(150) NOT NULL,
    lib_precio DECIMAL(10,2) NOT NULL
);