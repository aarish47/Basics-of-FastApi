# ----- INSTALLATION -----
#!pip install fastapi

# ----- IMPORTS -----
from fastapi import FastAPI # This is how you import the library
from enum import Enum

# ----- DEFINE THE APP -----
app = FastAPI() # Defining the app

# ----- ROUTE -----
@app.get("/home/{name}") # Defining the route

# ------ DEFINE THE FUNC -----
async def home(name):
    return f"Hello {name}, this is my first application on FastApi"

# To run the app on the cmd prompt type this command:
# uvicorn filename:app --reload

# We added the --reload so that whenever we make changes in our app
# we will not have to restart the server.

# ------------------------------ GET REQUEST -----------------------------------

# ----- CREATE A DATABASE -----]
class Available_Cuisines(str, Enum):
    italian = "italian"
    indian = "indian"
    chinese = "chinese"

food_items = {
    "italian": ["pizza", "burger", "pasta"],
    "indian": ["daal chawaal", "samosa", "butter chicken"],
    "chinese": ["sushi", "rice", "tai pan", "piyali"]
}

print(food_items)

# ----- ROUTE 2 -----
@app.get("/get/{cuisine}")
async def get(cuisine: Available_Cuisines):
    return {"food_items": food_items.get(cuisine)}
