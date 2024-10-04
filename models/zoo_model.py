from typing import Optional

from sqlmodel import Field, SQLModel

class Zoo(SQLModel, table=True):
    __tablename__: str = 'zoo'

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str  
    especie: str  
    idade: Optional[int] = Field(default=None) 
    habitat: Optional[str]  
    alimentacao: Optional[str]  
    peso: Optional[float] = Field(default=None)  
    status_conservacao: Optional[str] = Field(default=None) 