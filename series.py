# Importar modulo
import sqlite3

# Conexion
conexion = sqlite3.connect('series.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS series(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        serie_name varchar(255) NOT NULL,
        serie_clasificacion varchar(255) NOT NULL,
        serie_num_capitulos int(255) NOT NULL,
        serie_num_temporada int(255) NOT NULL,
        serie_poster text NOT NULL,
        serie_ranking text NOT NULL,
        serie_cast varchar(255) NOT NULL,
        serie_created_at varchar(255) NOT NULL,
        serie_property_of varchar(255) NOT NULL,
        serie_trailer boolean NOT NULL
        );
""")

# Guardar cambios
conexion.commit()

# Cerrar conexion
conexion.close()
