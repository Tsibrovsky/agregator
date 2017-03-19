from sqlalchemy import Column, Integer, String, Float
from database_init import Base, db_session


class Cities(Base):
    
    __tablename__='cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lat = Column(Float)
    lon = Column(Float)

    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat # широта і довгота, zip-код не всі підтримують
        self.lon = lon # по назві міста теж ненадійно

db_session.add_all([Cities('Cherkasy', '49.43', '32.06'),
                 Cities('Kharkiv', '50', '36.25'),
                 Cities('Odesa', '46.48', '30.73'),
                 Cities('Lviv', '49.84', '24.02'),
                 Cities('Donetsk', '48', '37.8')])
db_session.commit()






