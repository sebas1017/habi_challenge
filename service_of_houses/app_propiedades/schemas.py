from pydantic import BaseModel
from typing import List
class UserRequestModel(BaseModel):
    years: List
    cities: List
    status: List

