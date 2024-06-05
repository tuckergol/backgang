# README for Data Structures and Final Project

## Background

- This project consists of several integrated team features into one, unanimous project.
  - This is the backend for the project. The frontend README contains information regarding crediting and additional context.
- Template for the project was a teacher-provided flask porfolio containing many starter files to aid in building the base system(s) of backend functionality (ex: main.py).

###  Stock Project 
---
- Created by Varun Manoj Pillai ( varunm532 )
- Files used in this project: api/stock.py, api/stocksort.py, model/users.py, model/stockfilter.py
  - api/stock.py:
      - contain api endpoint code to:
          - diplay stocks data stored in SQLite3 db and update price through 3rd party api
          - code to handle buying and selling actions
          - code to sent data to frontend to create interactive graph through AnyChart
          - code to display all transactions of user (data from db)
          - code to update single stock
          - code to display sorted stocks based on sector
  - api/stocksort.py:
      - Code to recieve input from user about sectore selection
      - calls sorting program in model/stockfilter.py
      - returns truplet of sorted stocks
  - model/stockfileter.py:
      - code to clean CSV file containing all stocks from S&P 500
      - code to clean json responce to match clean csv data
      - code to bucket sort and code to sort stocks alphebetically
   
    
###  Painter Project 
---
- Created by Deva Sasikumar ( devaSas1 )
- Files used in this project: api/paint_api.py, model/painting.py
- api/paint_api.py:
    - contains API endpoint code to:
    - upload painting data and associate it with a user
    - display all paintings stored in the database along with the associated usernames
- model/painting.py:
    - defines the Painting model with attributes for image data and user association
    - contains the Painting class, which represents the Painting table in the database
    - userID: Foreign key linking the painting to a user
    - id: Primary key for identifying each painting uniquely
    - image: Text field to store the painting data
    - code to initialize the Painting table in the database

