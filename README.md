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
    
### Meme Maker
---
- Created by Tejas Manoj
- files for this feature: 2024-04-04-memmaker.md, memeforge.py, memeforge_functions.py, memeforge_database.py
  - 2024-04-04-mememaker.md's function:
    - Page Layout and Styling: Sets up the HTML structure and CSS styling for a "Meme Maker" webpage, with a title, input fields, and buttons.
    - Image and Text Input: Allows users to upload an image and enter text for the top and bottom of the meme.
    - Meme Generation: Uses JavaScript to send the image and text to an API to create the meme, and displays the generated meme on the page.
    - Meme Downloading: Provides a button for users to download the generated meme. 
  - memeforge.py's function: 
    - Imports and Setup: Imports necessary libraries for building a REST API with Flask, including Flask-RESTful for API creation and Flask-CORS for handling cross-origin requests. Sets up the blueprint for the meme forge API.
    - Meme Creation Endpoint: Defines a POST endpoint (/maker/) that accepts image and text data, generates a meme, and returns the meme image in base64 format. Optionally, it saves the meme to the database.
    - Database Query Endpoint: Defines a GET endpoint (/get_database) that returns all images stored in the database.
    - Add Image Endpoint: Defines a POST endpoint (/add_image) that allows adding a new image to the database.
    - Clear Database Endpoint: Defines a GET endpoint (/clear_database) that clears all entries in the database.
  - memeforge_functions.py's function:
    - Image to Base64 Conversion: Provides a function (imageToBase64) to convert an image into a base64-encoded string, useful for transmitting image data as text.
    - Base64 to Image Conversion: Includes a function (base64toImage) to decode a base64 string back into an image, allowing for the manipulation and display of images encoded as base64.
    - Meme Creation: Implements a function (meme_maker) that takes an image and adds top and bottom text to create a meme. It dynamically adjusts font size based on image dimensions and centers the text with an outline for better visibility.
    - Text Drawing on Image: Uses the ImageDraw and ImageFont modules from PIL to draw text with an outline on the image at specified positions, ensuring the text is visible against various backgrounds.
  - memeforge_database.py's function:
    - Imports and Setup: Imports necessary libraries, including SQLAlchemy for database interactions and PIL for image handling. Sets up the SQLAlchemy database model and initializes the Flask application context.
    - Database Initialization: Defines functions to initialize the database (initializeDatabase and initMeme) and create the necessary tables using SQLAlchemy's ORM.
    - Database Operations: Implements functions to manage database entries, including createImage for adding new images to the database, queryImages for retrieving all images from the database, and clearDatabase for deleting all entries.
    - Meme Model: Defines the Meme class as a SQLAlchemy model to represent meme data within the Flask application's database.
    - Images Model: Defines the Images class as a SQLAlchemy model to represent image data in a separate SQLite database, including columns for image name, function, and base64-encoded image data.
    
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

### House Price Prediction Project
---
- Created by Deva Sasikumar
- Files used in this project:
  - [api/house_price.py](api/house_price.py):
    - Contains API endpoint code for predicting house prices.
    - Utilizes Flask and Flask-RESTful for handling HTTP requests.
    - Implements a Linear Regression model trained on a dataset stored in 'house_prices.csv'.
    - Provides endpoints for preprocessing inputs, making predictions, and handling errors.


