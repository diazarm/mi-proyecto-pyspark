import os

# Forzamos a Spark a usar el Python del entorno virtual
os.environ["PYSPARK_PYTHON"] = os.path.join(os.getcwd(), "venv", "Scripts", "python.exe")

from pyspark import SparkContext

sc = SparkContext(appName="CacheEjemplo")

rdd = sc.parallelize([
    "Hola mundo",
    "Esto es una prueba",
    "Aprendiendo PySpark"
])

palabras = rdd.flatMap(lambda x: x.split(" ")).cache()

print("Conteo total:")
print(palabras.count())  # Ejecuta y cachea

print("Primera palabra:")
print(palabras.first())  # Usa la cache
