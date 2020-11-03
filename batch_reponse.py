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

    def send_json_results(self):
        samples = self._number_of_samples()
        (batches, last_batch_id) = self.create_batches()
        batches = self.convert_series_to_dict(batches)
        print({
            "rfw_id": self.id,
            "last_batch_id": last_batch_id,
            "number_of_samples": samples,
        })
        return {
            "rfw_id": self.id,
            "last_batch_id": last_batch_id,
            "samples": batches
        }

    def convert_series_to_dict(self, batches):
        batch_list = list()
        for batch in batches:
            dict_batch = batch.to_dict()
            batch_list.append(dict_batch)
        return batch_list

    def create_batches(self):
        batches = []
        column = self._get_column_from_csv()
        last_batch_id = self.batch_id
        for index in range(0, self.batch_size):
            batch = column[last_batch_id * self.batch_unit: (last_batch_id + 1) * self.batch_unit]
            batches.append(batch)
            last_batch_id += 1

        return batches, (last_batch_id - 1)

    def binary_result(self):
        samples = self._number_of_samples()
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

    # private methods

    def _get_column_from_csv(self):
        data_column = self.csv_data[self.metric]
        return data_column

    def _number_of_samples(self):
        return self.batch_size * self.batch_unit
