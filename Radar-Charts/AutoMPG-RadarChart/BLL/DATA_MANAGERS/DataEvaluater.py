from pandas import DataFrame
import pandas as pd
from pandas.core.series import Series
import numpy as np
from typing import Tuple


class DataEvaluater:

    data: DataFrame

    def __init__(self, data: DataFrame) -> None:
        self.data = data

    def __evaluate_mpg(self,val: float) -> int:
        scores = np.linspace(self.data.mpg.min(), self.data.mpg.max(), 5, endpoint=True)

        if 0 <= val <= scores[0]:
            return 1
        elif scores[0] <= val <= scores[1]:
            return 2
        elif scores[1] <= val <= scores[2]:
            return 3
        elif scores[2] <= val <= scores[3]:
            return 4
        elif scores[3] <= val <= scores[4]:
            return 5
        else:
            raise Exception("Out of Range")

    def __evaluate_cylinders(self, val: float) -> int:
        scoring = list(self.data.cylinders.unique())
        scoring.sort()

        if val == scoring[0]:
            return 1
        elif val == scoring[1]:
            return 2
        elif val == scoring[2]:
            return 3
        elif val == scoring[3]:
            return 4
        elif val == scoring[4]:
            return 5
        else:
            raise Exception("Out of Range")

    def __evaluate_horsepower(self, val: float) -> int:
        score = np.linspace(self.data.horsepower.min(), self.data.horsepower.max(), 5, endpoint=True)

        if 0 <= val <= score[0]:
            return 1
        elif score[0] <= val <= score[1]:
            return 2
        elif score[1] <= val <= score[2]:
            return 3
        elif score[2] <= val <= score[3]:
            return 4
        elif score[3] <= val <= score[4]:
            return 5
        else:
            raise Exception("Out of Range")

    def __evaluate_weight(self, val: float) -> int:
        scoring = np.linspace(self.data.weight.min(), self.data.weight.max(), 5, endpoint=True)

        if 0 <= val <= scoring[0]:
            return 5
        elif scoring[0] <= val <= scoring[1]:
            return 4
        elif scoring[1] <= val <= scoring[2]:
            return 3
        elif scoring[2] <= val <= scoring[3]:
            return 2
        elif scoring[3] <= val <= scoring[4]:
            return 1
        else:
            raise Exception("Out of Range")

    def __evaluate_acceleration(self, val: float) -> int:
        scoring = np.linspace(self.data.acceleration.min(), self.data.acceleration.max(), 5, endpoint=True)

        if 0 <= val <= scoring[0]:
            return 1
        elif scoring[0] <= val <= scoring[1]:
            return 2
        elif scoring[1] <= val <= scoring[2]:
            return 3
        elif scoring[2] <= val <= scoring[3]:
            return 4
        elif scoring[3] <= val <= scoring[4]:
            return 5
        else:
            raise Exception("Out of Range")

    def evaluate(self, row: Series) -> Tuple[str, list]:
        scores = []

        scores.append(self.__evaluate_mpg(row["mpg"]))
        scores.append(self.__evaluate_cylinders(row["cylinders"]))
        scores.append(self.__evaluate_horsepower(row["horsepower"]))
        scores.append(self.__evaluate_weight(row["weight"]))
        scores.append(self.__evaluate_acceleration(row["acceleration"]))

        scores.append(scores[0])
        name = str(row["name"]).upper()

        return name, scores

