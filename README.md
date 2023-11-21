# Parking Lot Information App

This is a simple FastAPI application that provides information about a parking lot, including available spaces, parking rates, and current status. It also displays parking spaces visually using rectangles.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/parking-app.git
   cd parking-app
    ```
2. Install the required dependencies
    ```
    pip install fastapi[all]
    ```
3. Run the FastAPI application:
    ```
    uvicorn parking:app --reload
    ```

4. Open your web browser and go to http://127.0.0.1:8000 to view the parking lot information.

## Files
* **parking.py**: FastAPI application code that defines the routes and serves the HTML template.
* **templates/index.html**: HTML template that displays parking lot information, parking spaces, and current status.
## Features
* Displays available spaces and parking rates.
* Visualizes parking spaces using rectangles.
* Shows the current status of the parking lot.
## Customization
You can customize the parking lot information by modifying the **lot_info** dictionary in the **parking.py** file.
```
lot_info = {
    "lot_name": "Joe's Smart Discount Parking",
    "available_spaces": 50,
    "price_per_hour": 5.0,
    "early_bird_discount": 2.0,
    "lot_status": "Open",  # Change the lot status here
}
```
Feel free to modify the HTML template to adjust the layout or add more features.

## Dependencies
* **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
## License
This project is licensed under the MIT License - see the LICENSE file for details.