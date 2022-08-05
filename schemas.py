from typing import Dict, List, Union
from pydantic import BaseModel


class Graph(BaseModel):
    id: int = None
    data: List[Dict[str, Union[str, int]]]

    class Config:
        orm_mode = True


class GraphIn(BaseModel):
    data: List[Dict[str, Union[str, int]]]

    class Config:
        orm_mode = True


class Routes(BaseModel):
    routes: List[Dict[str, Union[str, int]]]

    class Config:
        orm_mode = True


class MinRoute(BaseModel):
    distance: int
    path: List[str]

    class Config:
        orm_mode = True
