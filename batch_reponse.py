import pandas as pd
import json


class BatchResponse:
    def __init__(self, rfwId, benchType, metric, batchId, batchUnit, batchSize):
        self.rfwId = rfwId
        self.benchType = benchType
        self.metric = metric
        self.batchId = int(batchId)
        self.batchSize = int(batchSize)
        self.batchUnit = int(batchUnit)
        self.csv_data = pd.read_csv("./Workload-Data/" + benchType + ".csv")

    def send_json_results(self):
        samples = self.batchSize * self.batchUnit
        (batches, last_batch_id) = self.create_batches()
        batches = self.convert_series_to_dict(batches)
        print({
            "rfw_id": self.rfwId,
            "last_batch_id": last_batch_id,
            "number_of_samples": samples,
        })
        return {
            "rfwId": self.rfwId,
            "lastBatchId": last_batch_id,
            "samples": batches
        }

    def convert_series_to_dict(self, batches):
        batch_list = list()
        for batch in batches:
            dict_batch = batch
            batch_list.append(dict_batch)
        return batch_list

    def create_batches(self):
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
        (batches, last_batch_id) = self.create_batches()
        print({
            "rfw_id": self.id,
            "last_batch_id": last_batch_id,
            "number_of_samples": samples,
            "batches": batches
        })
        return {
            "rfw_id": self.id,
            "last_batch_id": last_batch_id,
            "number_of_samples": samples,
            "batches": batches
        }

