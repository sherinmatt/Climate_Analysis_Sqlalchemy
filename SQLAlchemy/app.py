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
#station
Station = Base.classes.station

#Flask
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate App!<br/>"
        f"Api Routes : <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )
#Precipitation Part

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

#Stations Part
#return json
@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)
    
    station_q = session.query(Station.station, Station.name).all()
    
    session.close()
    
    all_stations = list(np.ravel(station_q))
    return jsonify(all_stations)
                        

# TOBS Part  
# most ACTIVE Station
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
                        
#Temperature

                        
                        
    
        
        
        
       







