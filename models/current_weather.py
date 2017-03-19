from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.dialects.postgresql.json import JSONB
from database_init import Base, db_session


class CurrentWeather(Base):
    __tablename__='current_weather'
    id = Column(Integer, primary_key=True)
    provider = Column(String(50))
    location = Column(String(50))
    date = Column(TIMESTAMP)
    # поки що дані зберігаютья як є, без обробки
    current_weather = Column(JSONB)

    def __init__(self, provider, location, date, current_weather):
        self.provider = provider
        self.location = location
        self.date = date 
        self.current_weather = current_weather

    def __repr__(self):
        return f'current_weather: {self.current_weather}, date: {self.date}'

db_session.add_all([CurrentWeather('openweathermap', 'Cherkasy', datetime.now(), '1'),
                 CurrentWeather('worldweatheronline', 'Cherkasy', datetime.now(), '2'),
                 CurrentWeather('myweather2', 'Cherkasy', datetime.now(), '3')])
db_session.commit()


