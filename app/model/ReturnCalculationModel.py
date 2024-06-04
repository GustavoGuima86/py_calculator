from pydantic import BaseModel

from app.model.CalculationType import CalculationType


class ReturnCalculationModel(BaseModel):
    result: float
    calculation_type: CalculationType