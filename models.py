import reflex as rx
from sqlmodel import Field
from typing import Optional

class Modelos(rx.Model, table=True):
    """Modelos de casas."""
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str 
    descripcion: str
    precio: int 
    tags: str