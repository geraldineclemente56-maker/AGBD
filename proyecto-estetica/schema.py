from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship


engine = create_engine('sqlite:///mi_app.db', echo=True)
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


Base.metadata.create_all(engine)
print("¡base de datos y tablas creadas con éxito!")

