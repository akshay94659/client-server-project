import  buf_pb2,requests

rfwId = input('Enter the request for workload RFW-ID:  ')
benchMarkType = input('Enter one of the following options for chossing the data-set: such as DVD store or NDBench: ')
metric = input('Select one of the metrics from the following options on the Data Set:\n'
               '1. CPUUtilization_Average\n 2. NetworkIn_Average\n 3. NetworkOut_Average\n'
               ' 4. MemoryUtilization_Average\n')
batchId = input('Please enter the batchId to start the taking data in integer ')
batchUnit = input('Please enter the number of batches needed in one sample ')
batchSize = input('Please enter number of batches to be returned ')
dataType = input('Please enter the type of data-set you want to use: ')
dataAnalytics = input("Please Enter the data Analytics value you want to use:  ")
serializationType = input('Please enter the type of serialization/deserialization you want to use:\n 1. Press 1 for Json Type \n 2. Press 2 for Proto-Buf Type \n')

if(serializationType == "1"):
  res = requests.get("http://127.0.0.1:5000/getBachesJson?",
                     json={"rfwId": rfwId,
                           "benchType": benchMarkType,
                           "metric": metric,
                           "batchId": batchId,
                           "batchUnit": batchUnit,
                           "batchSize": batchSize,
                           "dataType": dataType,
                           "dataAnalytics":dataAnalytics,
                           }
                     )
  if res.status_code == 200:
        print(" rfwId: ", res.json()['rfwId'])
        print(" lastBatchId: ", res.json()['lastBatchId'])
        print(" Samples Requested: ", res.json()['samples'])
        print(" Data Analytics:",res.json()['dataAnalytics'])
  else:
        print ('Error Occurred')

elif(serializationType =="2") :

    batch_request = buf_pb2.Request()
    batch_request.id = rfwId
    batch_request.bench_type = benchMarkType
    batch_request.metric = metric
    batch_request.batch_id = int (batchId)
    batch_request.batch_unit = int (batchUnit)
    batch_request.batch_size = int (batchSize)
    batch_request.dataType = dataType
    batch_request.dataAnalytics = dataAnalytics

    res = requests.get("http://0.0.0.0:5000/getBatchesProtoBuf?", headers={'Content-Type': 'application/protobuf'},
                   data=batch_request.SerializeToString())

    batch_response = buf_pb2.Response.FromString(res.content)
    print(batch_response)
else:
  print("Invalid Input Entered");