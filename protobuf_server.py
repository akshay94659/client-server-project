from flask import Flask, request
from batch_reponse import BatchResponse
import batch_response_pb2
import json

batch_request = batch_response_pb2.Request
batch_response = batch_response_pb2.Response
app = Flask(__name__)


@app.route('/get_batches', methods=['GET'])
def get_batches():
    batch_request.id = request.args.get('id')
    batch_request.bench_type = request.args.get('bench_type')
    batch_request.metric = request.args.get('metric')
    batch_request.batch_unit = request.args.get('batch_unit')
    batch_request.batch_id = request.args.get('batch_id')
    batch_request.batch_size = request.args.get('batch_size')
    batch_object = BatchResponse(batch_request.id, batch_request.bench_type, batch_request.metric,
                                 batch_request.batch_unit, batch_request.batch_id, batch_request.batch_size)
    result = batch_object.binary_result()
    batch_response.number_of_samples = result['number_of_samples']
    batch_response.last_batch_id = result['last_batch_id']
    if batch_response.number_of_samples is not None and batch_response.last_batch_id is not None:
        return '''
        rfw_id: {}\n,
        last_batch_id: {}\n,
        number_of_samples: {}\n,
        batches: {}
        '''.format(batch_request.id, batch_response.last_batch_id, batch_response.number_of_samples, result['batches'])


if __name__ == '__main__':
    app.run(debug=True)  # run app in debug mode on port 5000
