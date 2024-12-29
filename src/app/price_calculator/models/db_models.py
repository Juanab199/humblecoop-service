from sqlalchemy import Column, Float, String, Integer
from alchemical import Model


class HumbleProviders(Model):
    __tablename__ = "providers"
    
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), unique=True)
    discount = Column(Float)
    


