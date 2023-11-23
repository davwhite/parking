from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# lot_info = {
#     "lot_name": "Joe's Cert Shop Parking",
#     "available_spaces": 10,
#     "price_per_hour": 5.0,
#     "early_bird_discount": 2.0,
#     "lot_status": "Lot Open",  # Add lot status
#     "reservations": 5  # Add reservations
# }

lot_info = {}
def load_lot_info():
    with open("../lot_info.json", "r") as file:
        lot_info = json.load(file)
    return lot_info

def create_zero_array(total_spaces):
    """Create an array of zeroes based on the total_spaces."""
    zero_array = [0] * total_spaces
    return zero_array

# # Example usage:
# total_spaces = 10
# zero_array = create_zero_array(total_spaces)
# print(zero_array)

lot_info = load_lot_info()

print("total_spaces: " + str(lot_info["total_spaces"]))

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "parking_info": lot_info})
