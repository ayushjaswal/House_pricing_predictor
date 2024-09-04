# House Price Predictor

## Overview

Welcome to the House Price Predictor project! This application uses a Linear Regression model, implemented in Python with Flask, to estimate house prices based on various features. The model is designed to provide accurate predictions by leveraging Linear Regression and Lasso techniques, with ongoing improvements to its accuracy.

## Features

- Predict house prices based on several input features.
- Utilizes Linear Regression and Lasso techniques for prediction.
- Web interface built with Flask for easy interaction.

## Installation

To set up this project locally, follow these steps:

### Prerequisites

- Python 3.6 or later
- pip (Python package installer)

### Clone the Repository

```
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
```

### Install Dependencies
Create a virtual environment (recommended) and install the required packages:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### Running the Application
Start the Flask application:
python application.py
By default, the application will be available at http://127.0.0.1:5000/.

## Usage
1. Navigate to the home page of the application.
2. Fill in the details about the house, such as area, number of bedrooms, bathrooms, etc.
3. Click the "Submit" button to get the predicted house price.

## Parameters Used
The model considers the following parameters for prediction:

- Area: Total area of the house (in square feet).
- Bedrooms: Number of bedrooms.
- Bathrooms: Number of bathrooms.
- Stories: Number of stories.
- Main Road: Whether the house is located on a main road.
- Guestroom: Presence of a guestroom.
- Basement: Presence of a basement.
- Hot Water Heating: Presence of hot water heating.
- Air Conditioning: Presence of air conditioning.
- Parking: Number of parking spaces.
- Preferred Area: Whether the house is in a preferred area.
- Furnishing Status: Furnishing status of the house (Furnished/Semi-Furnished/Unfurnished).
