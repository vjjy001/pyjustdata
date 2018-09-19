from flask import Flask
from flask import request
from flask import jsonify
from justdata.flask.rest.stock_rest import stock_rest_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(stock_rest_api)

@app.route('/')
def home_rest():
    
    return 'Welcome Home'


@app.route('/hello/<username>')
def hello_flask(username):
    return 'Hello {}'.format(username)


#test get post method
@app.route('/getkeyval',methods=['GET'])
def get_kv():
    
    #http://localhost:5000/getkeyval?name=james
    name = request.args.get('name')
    sex = request.args.get('sex')
    return 'name:{},sex:{}'.format(name,sex)


#get post json data
# { "name":"John", "age":30} http://localhost:5000/get_pdata
@app.route('/get_pdata',methods=['POST'])
def get_post_data():
    data = request.json
    #data = request.get_json() 
    print(type(data))
    print(data)
    #return data['name']+str(data['age'])
    return jsonify(data)

