from typing import List

from pydantic import BaseModel

from app.model.CalculationType import CalculationType


class RequestCalculationModel(BaseModel):
    numbers: List[int]
    calculation_type: CalculationType