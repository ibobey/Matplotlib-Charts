from BLL.PLOTTER.Plotter import *
from BLL.DATA_MANAGERS.RawDataManager import *
from BLL.DATA_MANAGERS.DataEvaluater import *
from random import randint

AutoMPG_file = r"BLL\DATA_MANAGERS\Automobile.csv"

if __name__ == "__main__":

    raw_data_manager = RawDataManager(raw_data_file_directory=AutoMPG_file)
    data = raw_data_manager.export_data()

    number_of_existing_car = data.shape[0]

    random_number = randint(0, number_of_existing_car)
    row_car_data = data.iloc[random_number]

    evaluater = DataEvaluater(data=data)

    car_scores = evaluater.evaluate(row=row_car_data)

    plotter = Plotter(data=car_scores)
    plotter.make_chart()


