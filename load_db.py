import reflex as rx
from models import Modelos
from sqlmodel import select

def main():
    print("=== Iniciando carga de datos ===")
    
    # FORZAR la creación de tablas
    print("🔧 Creando tablas...")
    rx.Model.create_all()
    print("✅ Tablas creadas")
    
    try:
        with rx.session() as session:
            # Intentar buscar registros existentes
            try:
                stmt = select(Modelos).where(Modelos.id == 1)
                existing = session.exec(stmt).first()
                
                if existing:
                    print(f"ℹ️ Ya existe: {existing.nombre}")
                    return
            except:
                # Si falla la consulta, continuamos con la inserción
                print("🔄 Tabla vacía, procediendo con inserción...")
            
            # Crear nuevo registro
            nuevo_modelo = Modelos(
                nombre="Casa Modelo A",
                descripcion="Casa de 120 m2 con 3 piezas y kit básico.",
                precio=45000000,
                tags="120",
            )
            
            session.add(nuevo_modelo)
            session.commit()
            session.refresh(nuevo_modelo)
            
            print(f"✅ Modelo creado exitosamente: {nuevo_modelo.nombre} (ID: {nuevo_modelo.id})")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()