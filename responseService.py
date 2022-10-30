import pandas as pd


class ResponseService:
    def __init__(self, rfwId, benchType, metric, batchId, batchUnit, batchSize,dataType,dataAnalytics):
        self.rfwId = rfwId
        self.benchType = benchType
        self.metric = metric
        self.batchId = int(batchId)
        self.batchSize = int(batchSize)
        self.batchUnit = int(batchUnit)
        self.dataType= dataType
        self.dataAnalytics= dataAnalytics
        self.csv_data = pd.read_csv("./Workload-Data/" + benchType+"-"+dataType + ".csv")

    def send_json_results(self):
        samples = self.batchSize * self.batchUnit
        (batches, lastBatchId) = self.create_batches()
        batches = self.convert_series_to_dict(batches)
        return {
            "rfwId": self.rfwId,
            "lastBatchId": lastBatchId,
            "samples": batches,
            "dataAnalytics" : self.dataAnalytics
        }

    def convert_series_to_dict(self, batches):
        batchList = list()
        for batch in batches:
            dictBatch = batch
            batchList.append(dictBatch)
        return batchList

    def createBatches(self):
        batches = []
        column = self.csv_data[self.metric]
        last_batch_id = self.batchId
        for index in range(0, self.batchSize):
            batch = column[last_batch_id * self.batchUnit: (last_batch_id + 1) * self.batchUnit].to_dict()
            batches.append(batch)
            last_batch_id += 1
        print(batches)

        return batches, (last_batch_id - 1)

    def binary_result(self):
        samples = self.batchSize * self.batchUnit
        (batches, lastBatchId) = self.createBatches()
        return {
            "rfw_id": self.id,
            "last_batch_id": lastBatchId,
            "number_of_samples": samples,
            "batches": batches
        }

