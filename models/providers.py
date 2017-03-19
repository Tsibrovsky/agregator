from sqlalchemy import Column, Integer, String
from database_init import Base, db_session


class Providers(Base):
    
    __tablename__='providers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    request_url = Column(String)
    
    def __init__(self, name, request_url):
        self.name = name
        self.request_url = request_url

     
db_session.add_all([Providers('openweathermap','http://api.openweathermap.org/data/2.5/weather?appid=11c0d3dc6093f7442898ee49d2430d20&units=metric'),
                    Providers('worldweatheronline','http://api.apixu.com/v1/current.json?key=c82bfc68fc1b41ebb8c132553171102'),
                    Providers('myweather2','http://www.myweather2.com/developer/forecast.ashx?uac=oFyMlJd4UG&output=json&temp_unit=c&ws_unit=mps')])
db_session.commit()

