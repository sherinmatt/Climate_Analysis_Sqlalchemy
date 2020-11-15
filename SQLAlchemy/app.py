#Hawaii Climate App

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

#reflect table
Base.prepare(engine, reflect = True)
#view classes
Base.classes.keys()


#measurement
Measurement = Base.classes.measurement
#Station
Station = Base.classes.station

#app = Flask(__name__)

#Flask Setup
app = Flask(__name__)

#Flask Path
@app.route("/")
def home():
    return (
        f"Welcome to the Hawaii Climate App!<br/>"
        f"The Api Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )
#Precipitation PART

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session = Session(engine)
    
    last_twelve_months = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    one_year_ago = dt.datetime.strptime(last_twelve_months,'%Y-%m-%d') - dt.timedelta(days = 365)
    
    d_precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).\
        order_by(Measurement.date).all()
    
    session.close()
    
#Return precipitation dictionary, 
#using values date, prcp
    precipitation_dict = []
    for date, prcp in d_precipitation:
        pre_dict = {}
        pre_dict['date'] = date
        pre_dict['prcp'] = prcp
    precipitation_dict.append(pre_dict)
    return jsonify(precipitation_dict)

#----------------
#Stations PART

#output station json_list
@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)
    
    station_q = session.query(Station.station, Station.name).all()
    
    session.close()
    
    all_stations = list(np.ravel(station_q))
    return jsonify(all_stations)

                        
#----------------
# TOBS PART 

# most Active Station
#also output a JSONIFied dict

@app.route("/api/v1.0/tobs")
def tobs_station(): 
    session = Session(engine)
                        
    datas_station = session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).all()
    
    most_active_station = datas_station[0][0]
                        
    session.close()
    
    tobs_dict = []
#date, tobs
    for date, tobs in most_active_station:
        m_dict = {}
        m_dict['date'] = date
        m_dict['tobs'] = tobs
    tobs_dict.append(m_dict)
    return jsonify(tobs_dict)
                        

#----------------
# Start Date PART

#make a start date query w/ : max temp, min temp, average temp
#output max, min , avg temp for all dates>= start date
#also output a JSONIFied dict

@app.route("/api/v1.0/<start>")
def start_dates(start): 
    
    session = Session(engine)
    
    date_results = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    session.close()
    
    starting_dict = []
    for max_temp, min_temp, avg_temp in date_results:
        s_dict = {}
        s_dict['max_temp'] = max_temp
        s_dict['min_temp'] = min_temp
        s_dict['avg_temp'] = avg_temp
        
    starting_dict.append(s_dict)
    print(f"For the starting date, the results are: {starting_dict}")
    return jsonify(starting_dict)

# Start and End Date PART 

#So, looking the start and end date range, show the max temp, min temp, avg temp
#also output a JSONIFied dict

@app.route("/api/v1.0/<start>/<end>")
def start_ends(start, end): 
    
    session = Session(engine)
    
    
    results = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()
    
    date_dict = []
    
    for max_temp, min_temp, avg_temp in results:
        e_dict = {}
        e_dict['max_temp'] = max_temp
        e_dict['min_temp'] = min_temp
        e_dict['avg_temp'] = avg_temp
        
    date_dict.append(e_dict)
    print(f"For the start-end dates, the results are: {date_dict}")
    return jsonify(date_dict)

if __name__ == '__main__':
    app.run(debug=True)

    
    
    


    
    


                        
                        
    
        
        
        
       







