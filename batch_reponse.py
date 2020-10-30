import pandas as pd
import json


class BatchResponse:
    def __init__(self, id, bench_type, metric, batch_unit, batch_id, batch_size):
        self.id = id
        self.bench_type = bench_type
        self.metric = metric
        self.batch_id = int(batch_id)
        self.batch_size = int(batch_size)
        self.batch_unit = int(batch_unit)
        self.csv_data = pd.read_csv("./data/" + bench_type + ".csv")

    def send_results(self):
        samples = self._number_of_samples()
        print(self.create_batches())
        return {
            "rfw_id": self.id,
            "last_batch_id": self.create_batches()[1],
            "number_of_samples": samples,
            "batches": self.create_batches()[0]
        }

    def create_batches(self):
        batches = []
        column = self._get_column_from_csv()
        last_batch_id = self.batch_id
        for index in range(0, self.batch_size):
            batch = column[last_batch_id * self.batch_unit: (last_batch_id + 1) * self.batch_unit]
            json_batch = batch.to_json()
            batches.append(json_batch)
            last_batch_id += 1

        return json.dumps(batches), last_batch_id

    # private methods

    def _get_column_from_csv(self):
        data_column = self.csv_data[self.metric]
        return data_column

    def _number_of_samples(self):
        return self.batch_size * self.batch_unit


# http://0.0.0.0/get_batches?id=1&bench_type=DVD-testing&metric=NetworkIn_Average&batch_unit=100&batch_id=2&batch_size=8