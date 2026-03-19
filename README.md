# Casas Living House

Aplicación web para **Casas Prefabricadas Living House**, empresa chilena del centro sur de Chile dedicada al desarrollo inmobiliario y construcción de viviendas prefabricadas de calidad.

Construida con **Reflex** — framework Python que compila a React en el frontend y FastAPI en el backend.

---

## Requisitos

- Python 3.10+
- Node.js 18+
- pip

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Jcastillomora/casaslivinghouse.git
cd casaslivinghouse
```

### 2. Crear y activar entorno virtual

```bash
# Windows
python -m venv lhenv
lhenv\Scripts\activate

# macOS / Linux
python -m venv lhenv
source lhenv/bin/activate
```

### 3. Instalar dependencias Python

```bash
pip install -r requirements.txt
```

### 4. Inicializar Reflex

```bash
reflex init
```

Este comando instala las dependencias de Node.js y genera la carpeta `.web/` (frontend compilado).

### 5. Agregar assets manualmente

Los archivos de media **no están incluidos en el repositorio** (imágenes, videos y catálogo). Deben colocarse en la carpeta `assets/` antes de ejecutar el proyecto.

**Catálogo de modelos** (obligatorio):
```
assets/Catálogo .xlsx
```
Debe contener la hoja `Hoja 1` con las columnas:
`id | modelo | superficie(m2) | dormitorios | baños | precio | descripción | imagen | url_imagen | plano`

**Imágenes de modelos:**
```
assets/lago_ranco_54.jpg
assets/7lagos_108.jpg
assets/volcan_osorno_137.jpg
assets/volcan_osorno_124.jpg
assets/volcan_osorno_150.jpg (o .pdf)
assets/puerto_octay_54.jpg
assets/puerto_octay_72.jpg
assets/puerto_octay_90.jpg
assets/puerto_varas_60.jpg
assets/puerto_varas_80.jpg
assets/puertonuevo_1a_36.jpg
assets/puertonuevo_2a_54.jpg
assets/foto_sección 1.jpg
```

**Fotos del equipo:**
```
assets/Alexander Saez.jpeg
assets/Juan Carlos Garcia.jpeg
```

**Videos testimoniales:**
```
assets/testimonio1.mp4
assets/testimonio2.mp4
assets/testimonio3.mp4
assets/testimonio4.mp4
```

### 6. Cargar datos iniciales

```bash
python load_db.py
```

Carga el catálogo de modelos desde `assets/Catálogo .xlsx` a la base de datos SQLite.

---

## Ejecución

### Modo desarrollo

```bash
reflex run
```

La app queda disponible en `http://localhost:3000` con hot reload automático.

### Modo producción (local)

```bash
reflex run --prod
```

---

## Despliegue en Reflex Cloud

```bash
# Autenticarse
reflex login

# Desplegar / actualizar
reflex deploy
```

---

## Estructura del proyecto

```
casaslivinghouse/
├── Casaslivinghouse/
│   ├── Casaslivinghouse.py   # Entry point, State, página index, catálogo
│   ├── state.py              # Estado global y filtros
│   ├── models.py             # Modelos de datos (rx.Base + SQLModel)
│   ├── navbar.py             # Barra de navegación responsive
│   ├── hero_section.py       # Sección hero con carousel de imágenes
│   ├── quienes_somos.py      # Sección del equipo
│   ├── testimonios.py        # Videos testimoniales
│   ├── como_comprar.py       # Proceso de compra paso a paso
│   ├── casa_detail.py        # Página de detalle por modelo /casa/[id]
│   ├── footer.py             # Footer con contacto
│   └── whatsapp.py           # Botón flotante de WhatsApp
├── assets/
│   ├── Catálogo .xlsx        # Fuente de datos de modelos
│   ├── style.css             # Estilos y animaciones globales
│   └── *.jpg / *.mp4         # Imágenes y videos
├── rxconfig.py               # Configuración de Reflex
├── requirements.txt          # Dependencias Python
└── load_db.py                # Script para cargar datos iniciales
```

---

## Comandos útiles

```bash
reflex run               # Servidor de desarrollo
reflex run --prod        # Producción local
reflex deploy            # Desplegar en Reflex Cloud
python load_db.py        # Recargar catálogo desde Excel
python check_db.py       # Verificar contenido de la base de datos
alembic upgrade head     # Aplicar migraciones de base de datos
```

---

## Contacto

**Casas Living House**
- WhatsApp: +56 9 3075 4516
- TikTok: [@casaslivinghouse](https://www.tiktok.com/@casaslivinghouse)
