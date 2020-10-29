import pandas as pd


class BatchResponse:
    def __init__(self, id, bench_type, metric, batch_unit, batch_id, batch_size):
        self.id = id
        self.bench_type = bench_type
        self.metric = metric
        self.batch_id = int(batch_id)
        self.batch_size = int(batch_size)
        self.batch_unit = int(batch_unit)
        self.last_batch_id = self.batch_id
        self.csv_data = pd.read_csv("./data/" + bench_type + ".csv")

    def send_results(self):
        samples = self.number_of_samples()
        return samples, self.id

    def number_of_samples(self):
        return self.batch_size * self.batch_unit

    def create_batches(self):
        batches = list()
        column = self._get_column_from_csv()
        for index in range(0, self.batch_size):
            batch = column[self.last_batch_id * self.batch_unit: (self.last_batch_id + 1) * self.batch_unit]
            batches.append(batch.to_json)
            self.last_batch_id += 1

    # private methods

    def _get_column_from_csv(self):
        data_column = self.csv_data[self.metric]
        return data_column




