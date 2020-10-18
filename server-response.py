from flask import Flask, request
import pandas as pd

app = Flask(__name__)


class BatchResponse:
    def __init__(self, id, bench_type, metric, batch_unit, batch_id, batch_size):
        self.id = id
        self.bench_type = bench_type
        self.metric = metric
        self.batch_id = int(batch_id)
        self.batch_size = int(batch_size)
        self.batch_unit = int(batch_unit)
        self.csv_data = pd.read_csv("./data/" + bench_type + ".csv")

    def process_results(self):
        return self.id


@app.route('/query')
def query():
    id = request.args.get('id')  # if key doesn't exist, returns None
    bench_type = request.args['bench_type']  # if key doesn't exist, returns a 400, bad request error
    metric = request.args.get('metric')
    batch_unit = request.args.get('batch_unit')  # if key doesn't exist, returns None
    batch_id = request.args['batch_id']  # if key doesn't exist, returns a 400, bad request error
    batch_size = request.args.get('batch_size')
    batch_object = BatchResponse(id, bench_type, metric, batch_unit, batch_id, batch_size)
    result = batch_object.process_results()
    if result is not None:
        return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)  # run app in debug mode on port 5000
