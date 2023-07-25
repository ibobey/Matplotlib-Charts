import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.series import Series
from pandas import DataFrame


class RawDataManager:

    __raw_data: DataFrame
    data: DataFrame

    def __init__(self, raw_data_file_directory: str):
        self.__read_data(directory=raw_data_file_directory)
        self.__drop_null_values()
        self.__get_original_data()

    def __read_data(self, directory: str):
        self.__raw_data = pd.read_csv(directory)

    def __drop_null_values(self):
        null_rows = list(self.__raw_data.loc[self.__raw_data.horsepower.isnull() == True].index)
        self.__raw_data.drop(null_rows, axis=0, inplace=True)
        self.__raw_data.reset_index(drop=True, inplace=True)

    def __get_original_data(self):
        self.data = self.__raw_data[["name", "mpg", "cylinders", "horsepower", "weight", "acceleration"]]
        del self.__raw_data

    def export_data(self):
        return self.data