import requests

id = input('Please Enter Request For Workload (RFW) ID:')
bench_type = input('Please Enter one of the following:\n 1. DVD-testing\n 2. DVD-training\n 3. NDBench-training\n'
                   '4. NDBench-training\n')
metric = input('Please choose one of the metrics from the following:\n'
               '1. CPUUtilization_Average\n 2. NetworkIn_Average\n 3. NetworkOut_Average\n'
               ' 4. MemoryUtilization_Average\n')
batch_id = input('Please Enter the Batch Id (from which batch you want the data to start from) in integer: ')
batch_unit = input('Please Enter the number of samples you want in one batch in integer: ')
batch_size = input('Please Enter the number of batches to be returned in integer: ')

res = requests.get("http://127.0.0.1:5000/get_batches?",
                   json={"id": id,
                         "bench_type": bench_type,
                         "metric": metric,
                         "batch_unit": batch_unit,
                         "batch_id": batch_id,
                         "batch_size": batch_size}
                   )
print(res.text)
