from flask import Flask, jsonify, request
import redis
import json

app = Flask(__name__)

# Connect to Redis
redis_host = 'localhost' # Change this if your Redis is on a different host.
redis_port = 6379 # Change this if your Redis is on a different port.
r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/exoplanets/<name>', methods=['GET'])
def get_exoplanet(name):
    data = r.get(name)
    if data:
        return jsonify(json.loads(data))
    else:
        return jsonify({"error": "Exoplanet not found!"}), 404

@app.route('/exoplanets', methods=['GET'])
def get_all_exoplanets():
    keys = r.keys('*')
    data = [json.loads(r.get(key)) for key in keys]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
