from flask import Flask, request
from batch_reponse import BatchResponse

app = Flask(__name__)


@app.route('/get_batches', methods=['GET'])
def get_batches():
    id = request.json['id']
    bench_type = request.json['bench_type']
    metric = request.json['metric']
    batch_unit = request.json['batch_unit']
    batch_id = request.json['batch_id']
    batch_size = request.json['batch_size']
    batch_object = BatchResponse(id, bench_type, metric, batch_unit, batch_id, batch_size)
    result = batch_object.send_json_results()
    if result is not None:
        return result


if __name__ == '__main__':
    app.run(debug=True)
