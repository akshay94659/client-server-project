import batch_pb2, requests


batch_request = batch_pb2.Request()

id = input('Please Enter Request For Workload (RFW) ID:')
bench_type = input('Please type one of the following:\n 1. DVD-testing\n 2. DVD-training\n 3. NDBench-training\n'
                   '4. NDBench-training\n')
metric = input('Please type one of the metrics from the following:\n'
               '1. CPUUtilization_Average\n 2. NetworkIn_Average\n 3. NetworkOut_Average\n'
               ' 4. MemoryUtilization_Average\n')
batch_id = int(input('Please Enter the Batch Id (from which batch you want the data to start from) in integer: '))
batch_unit = int(input('Please Enter the number of samples you want in one batch in integer: '))
batch_size = int(input('Please Enter the number of batches to be returned in integer: '))

batch_request.id = id
batch_request.bench_type = bench_type
batch_request.metric = metric
batch_request.batch_id = batch_id
batch_request.batch_unit = batch_unit
batch_request.batch_size = batch_size

res = requests.get("http://0.0.0.0:5000/get_batches?", headers={'Content-Type': 'application/protobuf'},
                   data=batch_request.SerializeToString())

batch_response = batch_pb2.Response.FromString(res.content)
print(batch_response)
