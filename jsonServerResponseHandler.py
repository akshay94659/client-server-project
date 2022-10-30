from flask import Flask, request, json
from responseService import ResponseService

app = Flask(__name__)


@app.route('/getBachesJson', methods=['GET'])
def get_batches():
    rfwId = request.json['rfwId']
    benchType = request.json['benchType']
    metric = request.json['metric']
    batchId = request.json['batchId']
    batchUnit = request.json['batchUnit']
    batchSize = request.json['batchSize']
    dataType =request.json['dataType']
    dataAnalytics = request.json['dataAnalytics']
    batchObj = ResponseService(rfwId, benchType, metric, batchId, batchUnit, batchSize,dataType,dataAnalytics)
    res = batchObj.send_json_results()
    if res is not None:
        return json.dumps(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
