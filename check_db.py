import reflex as rx
from models import Modelos

def verificar_datos():
    try:
        with rx.session() as session:
            modelos = session.query(Modelos).all()
            
            if modelos:
                print(f"✅ Se encontraron {len(modelos)} modelos:")
                for modelo in modelos:
                    print(f"  - ID: {modelo.id}, Nombre: {modelo.nombre}, Precio: ${modelo.precio:,}")
            else:
                print("❌ No se encontraron modelos en la base de datos")
                
    except Exception as e:
        print(f"❌ Error consultando la base de datos: {e}")

if __name__ == "__main__":
    verificar_datos()