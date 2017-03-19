from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.current_weather import CurrentWeather
from models.cities import Cities
from models.providers import Providers

engine = create_engine('postgresql://postgres:root@localhost:5432/weather')
Session = sessionmaker(bind=engine)
session = Session()


# методи, щоб прочитати записи в таблицях
def get_cities():
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(Cities).all():
        print("id is", city.id)
        print("name is", city.name)
        print("lat is", city.lat)
        print("lon is", city.lon)
#get_cities()


def get_current_weather():
    Session = sessionmaker(bind=engine)
    session = Session()
    for data in session.query(CurrentWeather).all():
        print("provader is", data.provider)
        print("location is", data.location)
        print("date is", data.date)
        print("weather data is", data.current_weather)
#get_current_weather()


def get_providers():
    Session = sessionmaker(bind=engine)
    session = Session()
    for provider in session.query(Providers).all():
        print("id of the provider is", provider.id)
        print("name of the provider is", provider.name)
        print("url of the provider is", provider.request_url)
#get_providers()

