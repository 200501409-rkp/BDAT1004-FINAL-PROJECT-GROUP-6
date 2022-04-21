from flask import Flask, render_template, json, template_rendered
from pymongo import MongoClient, DESCENDING

from dotenv import load_dotenv
from datetime import datetime
import requests
import pytz
import time
import os
import sys


load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    cityName = "Barrie"
    degSymbol = u'\N{DEGREE SIGN}'
    
    # Current Date & Time according to the Timezone
    new_timezone = pytz.timezone("Canada/Eastern")
    now = datetime.now()
    now = now.astimezone(new_timezone)
    s1 = now.strftime("%h %d, %I:%M %p")

    # MongoDB Credentials
    USER = os.getenv("MONGODB_USER")
    PASS = os.getenv("MONGODB_PASS")
    
    # Connection String to MongoDB
    client = MongoClient(f"mongodb+srv://{USER}:{PASS}@weather.fnjiw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
    # db & collection
    db = client["weatherDB"]
    hrCollection = db["hourlyWeather"]
    currCollection = db["currentWeather"]

    # Empty lists to collect hourly data
    hrTemp  = []; hrHumidity = []; hrIcons = []; hrTimes = []; hrDates = []; hrWeather = []

    # Extracting data from API response and appending to the above mentioned lists according to the data
    for hrData in hrCollection.find({}, {'_id':0}).sort("created", DESCENDING).limit(47):
        hrTemp.append(hrData['temp'])
        hrHumidity.append(hrData['humidity'])

        t = datetime.fromtimestamp(hrData['timestamp']).astimezone(new_timezone).strftime('%I %p')
        hrTimes.append(t)
        
        hrDates.append(time.strftime("%h %d, %Y", time.gmtime(hrData['timestamp'])))
        hrIcons.append(hrData['icon'])
        hrWeather.append(hrData['weather'].title())
    
    
    hrTemp.reverse(); hrHumidity.reverse(); hrTimes.reverse(); hrDates.reverse(); hrIcons.reverse(); hrWeather.reverse()

    currData = currCollection.find_one(sort=[("timestamp", DESCENDING)])
    currData['visibility'] = int(currData['visibility'])/1000
    
    return render_template('index.html', city=cityName, degSymbol=degSymbol, datetime=s1, current=currData, 
    hrIcons=hrIcons, hrTemp=json.dumps(hrTemp), hrHumidity=hrHumidity, hrTime=hrTimes, hrDates=hrDates, hrWeather=hrWeather)


if __name__ == "__main__":
    app.run()