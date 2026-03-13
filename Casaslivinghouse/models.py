from typing import Optional
import reflex as rx

class Casa(rx.Base):
    id: int
    modelo: str
    superficie_m2: int  # superficie(m2) del Excel
    dormitorios: int
    banos: int
    precio: int
    descripcion: str
    imagen: str  # URL externa de la imagen
    url_imagen: str  # Ruta local de la imagen
    plano: str  # URL del PDF del plano