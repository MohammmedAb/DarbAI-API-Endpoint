
# Saudi Landmark Classifier

## Overview

This project uses the FastAI framework to create a classifier that recognizes major landmarks in Saudi Arabia

## API and Deployment

The model is accessible through a simple REST API built with FastAPI. It's hosted on Railway. For more details, check out our [API Docs](https://fastapi-production-c2d8.up.railway.app/docs).

## Supported Landmarks

Our model is trained to identify the following Saudi landmarks:

- Al Masmak Palace
- Hegra
- Ithra
- Jabal AlFil (Elephant Rock)
- Kingdom Tower
- Maraya
- Nassif House Museum
- Quba Mosque
- Riyadh Water Tower
- The Clock Towers
- The Kaaba

## ✨ Features

- FastAPI
- [Hypercorn](https://hypercorn.readthedocs.io/)
- Python 3

## 💁‍♀️ How to use

- Clone locally and install packages with pip using `pip install -r requirements.txt`
- Run locally using `hypercorn main:app --reload`

