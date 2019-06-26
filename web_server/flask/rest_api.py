# import functions from the flask library
from flask import Flask, jsonify, request, abort

# create an app instance
app = Flask(__name__)

# create a devices resource
devices = [
    {
        "id": 0,
        "name": "NX-9K-1",
        "ip": "10.0.0.1"
    },
    {
        "id": 1,
        "name": "NX-9K-2",
        "ip": "10.0.0.2"
    }
]


# handle GET request
@app.route('/api/devices/', methods=['GET'])
def get_devices():
    return jsonify({'tasks': devices})


# handle POST request
@app.route('/api/devices/', methods=['POST'])
def post_device():
    #  check required parameters
    # if doesn't have all required parameters, return 404 error
    if not request.json or 'name' not in request.json or 'ip' not in request.json:
        abort(404)

    # generate device obj
    device = {
        "id": len(devices),
        "name": request.json['name'],
        "ip": request.json['ip']
    }

    # add device obj to devices resources
    devices.append(device)

    # return devices resources with 201 state code
    return jsonify({'task': devices}), 201


# main entry
if __name__ == '__main__':
    # run app when script is been execute
    # this will create a web server at port 8080, you can visit http://0.0.0.0:8080/
    app.run(host='0.0.0.0', port=8080, debug=True)
