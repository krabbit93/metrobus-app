import os

url_data = "https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=limite-de-las-alcaldias&q=&rows=16&facet=nomgeo"
url_db = f"mysql+mysqlconnector://" + os.environ["DB_USERNAME"] + ":" + os.environ["DB_PASSWORD"] +\
         "@" + os.environ["DB_HOST"] + ":" + os.environ["DB_PORT"] + "/" + os.environ["DB_DATABASE"]
