import numpy as np

from DataSynthesizer.datatypes.AbstractAttribute import AbstractAttribute
from DataSynthesizer.datatypes.utils.DataType import DataType


class FloatAttribute(AbstractAttribute):
    def __init__(self, name, is_candidate_key=False, is_categorical=False, histogram_size=20):
        super().__init__(name, is_candidate_key, is_categorical, histogram_size)
        self.is_numerical = True
        self.data_type = DataType.FLOAT

    def infer_domain(self, column):
        super().infer_domain(column)

    def generate_values_as_candidate_key(self, n):
        return np.arange(self.min, self.max, (self.min - self.max) / n)

    def sample_values_from_binning_indices(self, binning_indices):
        return super().sample_binning_indices_in_independent_attribute_mode(binning_indices)
