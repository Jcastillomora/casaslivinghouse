import duckdb

con = duckdb.connect("reflex.db")
con.execute("INSERT INTO modelos (nombre, descripcion, precio, tags) VALUES ('Casa Modelo B', 'Casa de 2000 m2 con 4 piezas y kit básico.', 95000000, '200')")
con.table("modelos").show()
con.close()