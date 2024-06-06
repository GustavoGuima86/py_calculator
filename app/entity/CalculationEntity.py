from sqlalchemy import Column, Integer, ARRAY, Enum, Float
from sqlalchemy.ext.declarative import declarative_base

from app.model.CalculationType import CalculationType

CalculationBase = declarative_base()
metadata = CalculationBase.metadata

class CalculationEntity(CalculationBase):
    __tablename__ = 'Calculation1'

    id = Column(Integer, primary_key=True, autoincrement=True)
    numbers = Column(ARRAY(Integer))
    calculation_type = Column(Enum(CalculationType))
    result = Column(Float)
