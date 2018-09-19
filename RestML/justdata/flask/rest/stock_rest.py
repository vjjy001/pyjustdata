from flask import  Blueprint
from flask import request
from justdata.ml.stock.fundstock import FundaHelper

stock_rest_api = Blueprint('stock_rest_api', __name__)



@stock_rest_api.route('/get_fund_data',methods=['GET'])
def get_fundamental_stock_data():
    ticker = request.args.get('ticker')
    print(ticker)
    fh = FundaHelper(str(ticker))
    return fh.get_zack_funda()
