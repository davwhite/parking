from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

lot_info = {
    "lot_name": "Joe's Cert Shop Parking",
    "available_spaces": 10,
    "price_per_hour": 5.0,
    "early_bird_discount": 2.0,
    "lot_status": "Lot Open",  # Add lot status
    "reservations": 5  # Add reservations
}

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "parking_info": lot_info})
