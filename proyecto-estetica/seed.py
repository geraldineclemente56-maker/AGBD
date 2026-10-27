from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///mi_app.db')
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=False)
    turnos = relationship("Turno", back_populates="cliente")

class Servicio(Base):
    __tablename__ = "servicios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    duracion_minutos = Column(Integer, nullable=False)
    turnos = relationship("Turno", back_populates="servicio")

class Profesional(Base):
    __tablename__ = "profesionales"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    turnos = relationship("Turno", back_populates="profesional")

class Turno(Base):
    __tablename__ = "turnos"
    id = Column(Integer, primary_key=True)
    fecha_hora = Column(DateTime, nullable=False)
    estado = Column(String, default="Pendiente")
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    servicio_id = Column(Integer, ForeignKey("servicios.id"))
    profesional_id = Column(Integer, ForeignKey("profesionales.id"))
    cliente = relationship("Cliente", back_populates="turnos")
    servicio = relationship("Servicio", back_populates="turnos")
    profesional = relationship("Profesional", back_populates="turnos")

db = SessionLocal()

print("🌱 Insertando datos de prueba...")

# 1. Crear Servicios
servicio1 = Servicio(nombre="Limpieza Facial Profunda", precio=18500.0, duracion_minutos=60)
servicio2 = Servicio(nombre="Lifting de Pestañas", precio=15000.0, duracion_minutos=45)
servicio3 = Servicio(nombre="Masajes Relax", precio=22000.0, duracion_minutos=50)

# 2. Crear Profesionales
profesional1 = Profesional(nombre="Camila Gómez", especialidad="Cosmiatra")
profesional2 = Profesional(nombre="Vanesa Rodas", especialidad="Lashista")

# 3. Crear Clientes
cliente1 = Cliente(nombre="Sofía Martínez", telefono="1123456789", email="sofia@gmail.com")
cliente2 = Cliente(nombre="Valentina Ríos", telefono="1198765432", email="valentina@gmail.com")

db.add_all([servicio1, servicio2, servicio3, profesional1, profesional2, cliente1, cliente2])
db.commit()

# 4. Crear un Turno de ejemplo
turno_ejemplo = Turno(
    fecha_hora=datetime(2026, 11, 10, 15, 30, 0),
    estado="Confirmado",
    cliente_id=cliente1.id,
    servicio_id=servicio1.id,
    profesional_id=profesional1.id
)

db.add(turno_ejemplo)
db.commit()

print("¡Datos de prueba insertados con éxito!")
db.close()