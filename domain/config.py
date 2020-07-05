import logging
import os
import sys
import time

"""
Constants that are used for script
"""
url_data_town_hall = "https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=limite-de-las-alcaldias&q=&rows=18&facet=nomgeo"

url_data_units_location = "https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=prueba_fetchdata_metrobus&rows=200&q="

url_db = f'mysql+mysqlconnector://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_DATABASE")}'

"""
Configure timezone
"""
os.environ['TZ'] = 'America/Mexico_City'
if 'tzset' in dir(time):
    time.tzset()

"""
Configure logs to simple stdout to console and file
"""
formatter = logging.Formatter("%(asctime)s %(levelname)s:%(message)s", "%Y-%m-%d %H:%M:%S")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)
logging.getLogger().setLevel(logging.INFO)


os.makedirs("/var/log/", exist_ok=True)
file_handler = logging.FileHandler("/var/log/metrobus_cron.log")
file_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_handler)
logging.getLogger().setLevel(logging.INFO)
