#!/bin/bash

# # Activate the virtual environment
source venv/bin/activate

# Create the apps database
python src/database.py

# Run the Python application
python src/app.py

