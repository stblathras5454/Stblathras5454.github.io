CS-340 MongoDB Dashboard (Enhanced Version)
Author: Steven Blathras
Course: SNHU CS-340: Advanced Programming Concepts

Overview:
This project is a data dashboard built using Dash, Plotly, and Dash Leaflet that connects to a MongoDB database (Animal Shelter - AAC). It allows filtering, visualizing, and mapping dog adoption data by rescue type. This enhanced version includes improved error handling, input validation, and a cleaner overall design. The project connects to a MongoDB server running locally and pulls data from the AAC.animals collection.

How to Run the Project:

Make sure Python 3.8 or higher is installed.

Install the required libraries: dash, dash-leaflet, pandas, matplotlib, and pymongo.

Ensure MongoDB is installed and running on your machine at localhost on port 27017.

Make sure the AAC.animals collection is already loaded into the MongoDB database.

Open the project folder in VS Code or another editor.

Launch Jupyter Notebook in the terminal from the same directory.

Open the ProjectTwoDashboard_Enhanced.ipynb file.

Run all cells to start the dashboard interface.

Files Included:

ProjectTwoDashboard_Enhanced.ipynb – The enhanced dashboard interface.

AnimalShelter.py – The refactored CRUD module with improvements.

README.md – This file (plain text version).

Notes:

No MongoDB authentication is required in this version. If you use credentials, update the connection string in AnimalShelter.py accordingly.

This version uses default local paths and assumes you run the notebook from the root of the project folder.

The dashboard will open in your browser and allow you to interactively explore and filter animal shelter data.