from flask import Flask, jsonify, request
import redis
import json

app = Flask(__name__)

# Connect to Redis
redis_host = 'redis-service.default.svc.cluster.local'
redis_port = 6379
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

@app.route('/exoplanet-names', methods=['GET'])
def get_exoplanet_names():
    keys = r.keys('*')
    return jsonify(keys)

if __name__ == "__main__":
    app.run(debug=True)
