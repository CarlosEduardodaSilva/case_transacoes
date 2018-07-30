from flask import Flask, request
from flask_restful import Resource, Api,reqparse
from flask_jsonpify import jsonify
import json
import pandas as pd

db = pd.read_csv("transactions.csv", sep='\t', delimiter=';', encoding='utf-8', index_col=False)

app = Flask(__name__)
api = Api(app)


class Transactions_Acquirer(Resource):
    def get(self, acquirer_name):
        query = db[db['AcquirerName'] == acquirer_name]
        dictionary = query
        dictionary = {'result': dictionary.to_dict('records')}
        #return json.dumps(dictionary, sort_keys=False, ensure_ascii=False, indent=4)
        return jsonify(dictionary)


class Transactions_Bandeira(Resource):
    def get(self, bandeira):
        query = db[db['CardBrandName'] == bandeira]
        dictionary = query
        dictionary = {'result': dictionary.to_dict('records')}
        #return json.dumps(dictionary, sort_keys=False, ensure_ascii=False, indent=4)
        return jsonify(dictionary)


class Transactions_CNPJ(Resource):
    def get(self, cnpj):
        query = db[db['MerchantCnpj'] == cnpj]
        dictionary = query
        dictionary = {'result': dictionary.to_dict('records')}
        #return json.dumps(dictionary, sort_keys=False, ensure_ascii=False, indent=4)
        return jsonify(dictionary)


class Transactions_Data(Resource):
    def get(self, data):
        query = db[db['AcquirerAuthorizationDateTime'] == data]
        dictionary = query
        dictionary = {'result': dictionary.to_dict('records')}
        #return json.dumps(dictionary, sort_keys=False, ensure_ascii=False, indent=4)
        return jsonify(dictionary)

api.add_resource(Transactions_Acquirer, '/acquirers/<acquirer_name>')
api.add_resource(Transactions_Bandeira, '/bandeira/<bandeira>')
api.add_resource(Transactions_CNPJ, '/cnpj/<cnpj>')
api.add_resource(Transactions_Data, '/data/<data>')


if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(port='5002')