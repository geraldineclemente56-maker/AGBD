from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine('sqlite:///mi_app.db')
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Servicio(Base):
    __tablename__ = "servicios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    duracion_minutos = Column(Integer, nullable=False)

class Profesional(Base):
    __tablename__ = "profesionales"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)

db = SessionLocal()

print("==============================")
print("LISTA DE CLIENTES REGISTRADOS:")
print("==============================")
clientes = db.query(Cliente).all()
for c in clientes:
    print(f"- ID: {c.id} | Nombre: {c.nombre} | Telefono: {c.telefono} | Email: {c.email}")

print("\n==============================")
print("LISTA DE SERVICIOS:")
print("==============================")
servicios = db.query(Servicio).all()
for s in servicios:
    print(f"- {s.nombre} | Precio: ${s.precio} | Duracion: {s.duracion_minutos} mins")

print("\n==============================")
print("LISTA DE PROFESIONALES:")
print("==============================")
profesionales = db.query(Profesional).all()
for p in profesionales:
    print(f"- {p.nombre} ({p.especialidad})")

db.close()