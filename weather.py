from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from datetime import datetime

def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

config_dict = get_default_config()
config_dict['language'] = 'ru'

def weather_status(city):
	owm = OWM('22fda27c3d82aa9208e50fe8721d8a6b', config_dict)
	mgr = owm.weather_manager()
	try:
		observation = mgr.weather_at_place(city)
	except Exception:
		return 'Город ' + city + ' не найден!'

	w = observation.weather
	temperature = w.temperature('celsius')

	# получим значения температуры
	temp_min = int_r(temperature['temp_min'])
	temp_max = int_r(temperature['temp_max'])

	temp_status = str(temp_min)

	if temp_min != temp_max:
		temp_status = temp_status + "..." + str(temp_max)

	feels_l = int_r(temperature['feels_like'])

	# получим прочие параметры: ветер, осадки, облачность, давление

	# параметры ветра:
	wind = w.wind()

	wind_speed = wind['speed']
	wind_deg = wind['deg']
	wind_str = ''

	if 0 <= wind_deg <= 22:
		wind_str = 'C'
	elif 23 <= wind_deg <= 67:
		wind_str = 'СВ'
	elif 68 <= wind_deg <= 112:
		wind_str = 'В'
	elif 113 <= wind_deg <= 157:
		wind_str = 'ЮВ'
	elif 158 <= wind_deg <= 202:
		wind_str = 'Ю'
	elif 203 <= wind_deg <= 247:
		wind_str = 'ЮЗ'
	elif 248 <= wind_deg <= 292:
		wind_str = 'З'
	elif 293 <= wind_deg <= 337:
		wind_str = 'СЗ'
	elif 338 <= wind_deg <= 360:
		wind_str = 'С'

	today = datetime.now()
	dt = today.strftime("%Y.%m.%d %H:%M:%S")

	result = '🌏 ' + city + ", " + str(dt) \
			+ '\n-------------------------------' \
			+ '\n🌂 За окном: ' + w.detailed_status \
			+ '\n🌡️ Температура: '  + temp_status + " °C" \
			+ '\n🗿 Ощущуется как: ' + str(feels_l) + " °C" \
			+ '\n💨 Ветер: ' + wind_str + ", " + str(wind_speed) + " м/с"

	return result