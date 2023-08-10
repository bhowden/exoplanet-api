# Exoplanet API

This is a simple Flask API to interact with exoplanet data stored in Redis.

## Requirements

- Python 3.8+
- Flask
- Redis
- A Kubernetes environment (if deploying within Kubernetes)

## Setup

1. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

2. If you're running this API within a Kubernetes cluster and you have your Redis service deployed there, set the `redis_host` in `api.py` to:

   ```python
   redis_host = 'redis-service.default.svc.cluster.local'
   ```

   This is the Kubernetes service DNS name which will route traffic to the correct Redis instance within the cluster.

## Running the API

1. Run the API:

   ```bash
   python api.py
   ```

2. Access the API:

   - To fetch a specific exoplanet by name: `http://<your_host>:80/exoplanets/<name>`
   - To fetch all exoplanets: `http://<your_host>:80/exoplanets`

## Docker

You can also build and run this API using Docker. Refer to the provided `Dockerfile` for details.

---

The `README.md` now includes the necessary instructions for setting up the Flask API with the appropriate Redis endpoint when deploying within a Kubernetes environment.