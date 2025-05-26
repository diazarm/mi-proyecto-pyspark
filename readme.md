````markdown
# 🧠 Proyecto PySpark - Conteo de Palabras con Cache

Este proyecto demuestra cómo usar PySpark en un entorno local para procesar texto, aplicar transformaciones y utilizar `.cache()` para evitar cálculos repetidos.

## 🚀 Requisitos

- Python 3.7 o superior
- pip
- Virtualenv (opcional, pero recomendado)

## ⚙️ Instalación

1. **Clonar el repositorio** (o crear tu carpeta de proyecto):

```bash
git clone https://github.com/diazarm/mi-proyecto-pyspark.git
cd mi-proyecto-pyspark
````

2. **Crear y activar el entorno virtual**:

```bash
python -m venv venv
# Activar:
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```
Si no tienes instalado pyspark, lo puedes hacer con este comando:
```bash
pip install pyspark
```
Luego este otro para que te genere el archivo donde estaran las dependencias. 
```bash
pip freeze > requirements.txt
```
3. **Instalar dependencias**:

```bash
pip install -r requirements.txt
```

## 🧪 Ejecución del proyecto

Para correr el script principal:

```bash
python main.py
```

Deberías ver la cantidad de palabras procesadas y la primera palabra detectada.

## 📦 Estructura del proyecto

```
mi-proyecto-pyspark/
├── venv/                 # Entorno virtual (no subir a Git)
├── main.py               # Script principal con PySpark
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Esta documentación
```

## 🧠 Conceptos incluidos

* RDDs en PySpark
* Transformaciones: `flatMap`, `filter`, `map`
* Acciones: `count()`, `first()`
* Uso de `.cache()` para optimizar procesamiento

## 📚 Recursos útiles

* [Documentación oficial de PySpark](https://spark.apache.org/docs/latest/api/python/)
* [Guía de RDDs](https://spark.apache.org/docs/latest/rdd-programming-guide.html)

---

💬 Si tenés preguntas, abrí un issue o escribime al [mail](marceloardiaz@gmail.com)

```

---

