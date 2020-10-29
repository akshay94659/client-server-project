from flask import Flask, request
from batch_reponse import BatchResponse

app = Flask(__name__)


@app.route('/get_batches', methods=['GET'])
def get_batches():
    id = request.args.get('id')  # if key doesn't exist, returns None
    bench_type = request.args.get('bench_type')  # if key doesn't exist, returns a 400, bad request error
    metric = request.args.get('metric')
    batch_unit = request.args.get('batch_unit')  # if key doesn't exist, returns None
    batch_id = request.args.get('batch_id')  # if key doesn't exist, returns a 400, bad request error
    batch_size = request.args.get('batch_size')
    batch_object = BatchResponse(id, bench_type, metric, batch_unit, batch_id, batch_size)
    result = batch_object.send_results()
    if result is not None:
        return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)  # run app in debug mode on port 5000
