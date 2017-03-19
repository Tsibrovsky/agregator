from flask import Flask,  render_template, request
from database_init import init_db, db_session
from models.current_weather import CurrentWeather
from datetime import datetime, timedelta
from models.cities import Cities
from models.providers import Providers

app = Flask(__name__)
app.config.from_object(__name__)

init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/current_weather', methods=['POST'])
def get_current_weather():
    query = db_session.query(CurrentWeather.current_weather, CurrentWeather.date).filter(
        CurrentWeather.location == request.form['city'],
        CurrentWeather.provider == request.form['api']).all()[-1]
    # виведе погодні дані з бд, якщо вони є і не старіші 2 годин
    if query != None and query[1] >= (datetime.now() - timedelta(hours=2)):  # timedelta(days=1, hours=2, seconds=15)
        # вивід данних користувачу
        data = query[0]
    else:
        # видалення старого запису з бд, хоча можна не видаляти якщо потрібна статистика
        db_session.query(CurrentWeather).filter(CurrentWeather.location == request.form['city'],
                                             CurrentWeather.provider == request.form['api']).delete()
        db_session.commit()
        # вибір з бд url провайдера та широти і довготи міста для запиту до апі
        provider_url = db_session.query(Providers.request_url).filter(Providers.name == request.form['api']).first()
        lat_lon = db_session.query(Cities.lat, Cities.lon).filter(Cities.name == request.form['city']).first()
        ''' затит до апі, тут у кожного провайдера свій параметр для місця для якого потрібні погодні данні
            або вивести ці if-и в окрему функцію, або під кожний провайдер робити специфічний метод
            можливий варіант зробити базовий клас Providers() і від нього субкласи по кожному конкретному апі
            з власними методами
        '''
        if request.form['api'] == 'openweathermap':
            params = {'lat': lat_lon[0], 'lon': lat_lon[1]}
        elif request.form['api'] == 'worldweatheronline':
            params = {'q': lat_lon}
        elif request.form['api'] == 'myweather2':
            params = {'query': lat_lon}
        # власне сам запит
        res = request.get(provider_url[0], params)
        # вивід данних користувачу
        data = res.json()
        # збереження оновлених данних в бд, преред збереженням їх потрібно перебрати, виділити темпер, швид вітру і т.д.
        obj_for_save_in_db = CurrentWeather(request.form['api'], request.form['city'], datetime.now(),
                                            current_weather=data)
        db_session.add(obj_for_save_in_db)
        db_session.commit()

    return render_template('current_weather.html', data=data)


if __name__ == '__main__':
    app.run()
