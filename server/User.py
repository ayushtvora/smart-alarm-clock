from datetime import datetime


class User:
    def __init__(self, name, email, password_hash, salt, time_zone):

        self.info = Info(name, email, password_hash, salt, time_zone)
        self.settings = Settings()
        self.alarms = []

class Info:
    def __init__(self, name, email, password_hash, salt, time_zone):
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.salt = salt
        current_time = datetime.now()
        self.created_at = self.created_at = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.created_at_epoch = current_time.timestamp()
        self.updated_at = self.created_at
        self.updated_at_epoch = self.updated_at
        self.time_zone = time_zone

class Settings:
    def __init__(self):
        self.snooze_length = 9
        self.volume = 50
        self.gradual_volume = True
        self.bedtime_reminders = True
        self.work_address = ""
        self.announcement_settings = AnnouncementSettings()

class AnnouncementSettings:
    def __init__(self):
        self.message = "Good Morning!"
        self.traffic = False
        self.weather = True
        self.weather_report = WeatherReport()
        self.stocks = False
        self.tasks = False
        self.calendar = False
        self.random_fact = False

class WeatherReport:
    def __init__(self):
        self.condition = True
        self.min_max_temp_c = False
        self.avg_temp_c = True
        self.total_precip_mm = False
        self.will_rain = False
        self.chance_of_rain = False
        self.will_snow = True
        self.chance_of_snow = False
        self.max_wind_kph = False
        self.uv_index = False
        self.sunrise = False
        self.sunset = False

class Alarm:
    def __init__(self, time, name="New Alarm", repeat=False, repeat_days=None, snooze=True, sound=0, enabled=True):
        self.name = name
        self.time = time
        self.repeat = repeat
        if repeat_days is None:
            self.repeat_days = []
        else:
            self.repeat_days = repeat_days
        self.snooze = snooze
        self.sound = sound
        self.enabled = enabled
        self.challenges = Challenges()

class Challenges:
    def __init__(self):
        self.math = False
        self.memory = False
        self.typing = False
        self.qr_code = False
        self.reaction = False