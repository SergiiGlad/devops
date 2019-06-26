# import flask library
from flask import Flask

# create an app instance
app = Flask(__name__)

# define url router, this function will respond when a user visits "/"
@app.route('/')
def hello_world():
    return 'Hello, World!'

# define url router, this function will respond when a user visits "/devnet"
@app.route('/devnet')
def hello_devnet():
    return 'Hello, DevNet!'

# main entry
if __name__ == '__main__':
    # run app when the script is executed
    # this will create a web server at port 8080, you can visit http://0.0.0.0:8080/ and http://0.0.0.0:8080/devnet
    app.run(host='0.0.0.0', port=8080, debug=True)
