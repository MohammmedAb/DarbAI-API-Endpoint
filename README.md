> Our DarbAI-API-Endpoint is seamlessly integrated into the Darb-AI website, managed in a separate repository: [MOHAMMAD-ALSUBAIE/Darb-AI.](https://github.com/MOHAMMAD-ALSUBAIE/Darb-AI)

# DarbAI-API-Endpoint

## Overview

This Repo serves as a API endpoint for two features in our DarbAI Project. 
1. The first feature is the **personalized trip planner feature**: which is used to plan a trip for the user based on their preferences.
2. The second feature is the **landmark recognition feature**: which is used to identify landmarks in Saudi Arabia and provide information about them.

## API and Deployment

The landmark recognition model and 
the trip planner model are both accessible through a simple REST API built with FastAPI. It's hosted on Railway. For more details, check out our [API Docs](https://fastapi-production-c2d8.up.railway.app/docs).

## How it works
### Trip Planner
![AI-Powered Itineraries drawio](https://github.com/MohammmedAb/DarbAI-API-Endpoint/assets/83492447/f171b347-f1af-4df4-8dc8-2e70008f6e3a)

### Landmark Recognition
![Landmark Recognition](https://github.com/MohammmedAb/DarbAI-API-Endpoint/assets/83492447/926e97b7-2d33-4e94-8927-7fd7238e4497)


## Supported Landmarks

Our model is trained to identify the following Saudi landmarks:

- Al Faisaliah Tower
- Al Masmak Palace
- Al Rahmah Mosque
- Diriyah
- Hegra
- Ibrahim Palace
- Ithra
- Jabal AlFil (Elephant Rock)
- King Abdullah Financial District (KAFD)
- Kingdom Tower
- Maraya
- Nassif House Museum
- Quba Mosque
- Riyadh Water Tower
- The Clock Towers
- The Kaaba

## ✨ Technologies

- FastAPI
- [Hypercorn](https://hypercorn.readthedocs.io/)
- Python 3
- PyTorch
- Fastai
- Railway


## 💁‍♀️ How to use

- Clone locally and install packages with pip using `pip install -r requirements.txt`
- Run locally using `hypercorn main:app --reload`
- you can now access the API at `http://localhost:8000/docs`
- you can acces the landmark recognition feature at `http://localhost:8000/landmark`
- but you can't access the trip planner feature locally because it requires a database connection which is not available locally

