Project Two Dashboard – CS 340
Created by: Steven Blathras
Technologies: Dash (Plotly), Python, MongoDB

Project Overview:
This project is an interactive dashboard built using Dash (by Plotly), showcasing data from an animal shelter MongoDB database. The dashboard filters dogs by rescue type, displays their location on a map, and visualizes breed distribution in a bar chart.

Prerequisites:
Before running the project, make sure you have the following installed:

Python 3.x

pip (Python package manager)

A virtual environment (recommended)

Required Python Packages:
Install the necessary packages via pip:
pip install dash pandas dash-leaflet matplotlib pymongo jupyterlab jupyter-dash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt  # optional, if you created this file

File Structure:
ProjectTwo/
│
├── AnimalShelter.py          # MongoDB CRUD operations module
├── ProjectTwoDashboard.ipynb # Jupyter Notebook for dashboard
├── assets/                   # (Optional folder for images like Glogo.png)

MongoDB Configuration:
Make sure your MongoDB instance is running (locally or on Atlas).
In AnimalShelter.py, edit the connection line:
self.client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>")

Replace with your own credentials.

How to Run the Dashboard in Jupyter Notebook:

Launch Jupyter Notebook or JupyterLab.

Open ProjectTwoDashboard.ipynb.

Run all cells. The dashboard will display inside the notebook using JupyterDash.

Note: If you see a deprecation warning for JupyterDash, the notebook will still work as expected.

