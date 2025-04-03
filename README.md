# BMI Calculator

## Overview
The BMI Calculator is a Python-based desktop application that allows users to input their health-related data and compute their Body Mass Index (BMI). The application is designed using `customtkinter` for a modern and user-friendly interface.

## Features
- User-friendly GUI built with `customtkinter`
- Input fields for Name, Age, Height, Weight, Steps, Water Intake, and Heart Rate
- BMI calculation based on height and weight
- Data storage using JSON files for future reference
- Error handling to ensure valid user input

## Installation
### Prerequisites
Ensure you have Python installed (Python 3.x recommended). You also need to install the required dependencies:

```sh
pip install customtkinter
```

## Usage
Run the application by executing the `main.py` script:

```sh
python main.py
```

## Project Structure
```
├── main.py          # Handles UI and initializes the application
├── buttonLogic.py   # Handles button interactions, BMI calculations, and file handling
├── userInput.py     # Manages user input validation and retrieval
├── calculations.py  # Contains the BMI calculation logic
```

## Code Explanation
- **`main.py`**: Defines the `App` class that sets up the GUI using `customtkinter`. It creates input fields, buttons, and a text display area.
- **`userInput.py`**: Defines the `userInput` class, which retrieves and validates user inputs.
- **`buttonLogic.py`**: Defines the `buttonLogic` class to handle button actions like updating and displaying user data.
- **`calculations.py`**: Contains the `bmiCalculator` class, which calculates BMI based on user input.

## BMI Calculation Formula
The BMI is calculated using the formula:

```python
BMI = weight / (height ** 2)
```
Where:
- `weight` is in kilograms
- `height` is in meters

## Error Handling
- If the user enters an invalid input (e.g., non-numeric values for age or height), the program displays an error message in the text display area.
- JSON file handling ensures that user data is stored properly, and missing files do not crash the program.

## Future Improvements
- Add a feature to classify BMI results into categories (Underweight, Normal, Overweight, etc.).
- Implement a graphical representation of BMI trends.
- Enhance the UI with more customization options.

## License
This project is open-source and available for modification and distribution.

---
Developed for VitalTech as a modular, maintainable, and scalable application.

