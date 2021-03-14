# sqlalchemy-challenge

# SQLALCHEMY SURFS UP

   # Background
      * Utilizing Hawaii climate database to conduct climate analysis 
      
   # Objective
      *  The main goal is to conduct climate data analysis through SQLAlchemy and by a building a flask

   # Database Source
   [Data](https://github.com/sherinmatt/sqlalchemy-challenge/tree/main/SQLAlchemy/Resources)
  
   # Technologies used:
      * Flask
      * NumPy
      * SQLAlchemy
      * Pandas
      * Matplotlib
      * Datetime
      
   ## Step 1:
   
    For the Precipitation analysis
      *  Worked on building a query using the latest year data- to get the date and prcp values. 
      *  After the analysis, plotted a diagram using dataframe plot method.

   ![alt](https://github.com/sherinmatt/sqlalchemy-challenge/blob/main/SQLAlchemy/Images/fig1.png)
      *  Lastly, also displayed a precipitation data summary statistics.

    For the Station analysis:
      * Worked on building a query to find the list of stations, in a descending order.
      * Also, found out which was the most active station.
      * Later, found out the most active station during the lastest year and created a histogram to showcase the temperature observation datas 
     
   ![alt](https://github.com/sherinmatt/sqlalchemy-challenge/blob/main/SQLAlchemy/Images/fig2.png)

   ## Step 2:
    
    Hawaii Climate App

      * Built a Climate Flask API

    Routes:
      * (/) - Home or starting page
      * (/api/v1.0/precipitation) - Created a query from latest precipitation datas. And, then, outputed all the data in a JSONified dictionary form
      * (/api/v1.0/stations) - Listed the names of stations. 
      * (/api/v1.0/tobs) - Furthermore, looked at the most active station in the latest year and made a query for temperature observations, date. Returned all the data in a JSONified dictionary form
      * (/api/v1.0/<start>) Made a query for the starting date and outputed the max, min and average temperature. Outputed all the data in a JSONified dictionary form.
      * (/api/v1.0/<start>/<end>) Made a query for the starting /ending date range, that showed the max, min and average temperature. Outputed all the data in a JSONified dictionary form.


   ## Inspiration
      Rutgers Bootcamp
