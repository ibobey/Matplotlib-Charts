import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray,pi
from typing import NoReturn, Tuple


class Plotter:

    data: tuple

    __categories: list
    __x: ndarray

    def __init__(self, data: Tuple[str, list]) -> None:
        self.data = data

        self.__set_categories()
        self.__set_radional_xscale()

    def __set_categories(self) -> NoReturn:
        self.__categories = ['MPG', 'CYLINDER', 'HP', 'WEIGHT', 'ACCELERATION', ""]

    def __set_radional_xscale(self) -> NoReturn:
        self.__x = np.linspace(start=0, stop= 2*pi, num=len(self.data[1]))

    def __set_theme(self):
        sns.set_theme(style="ticks", palette="pastel")
        sns.set_context("paper")

    def make_chart(self) -> NoReturn:
        self.__set_theme()

        x = self.__x
        y = self.data[1]
        name = self.data[0]

        plt.figure(figsize=(6,6))
        plt.subplot(polar=True)
        plt.ylim(0, 5)
        plt.thetagrids(np.degrees(x), labels=self.__categories)

        plt.plot(x,
                 y,
                 color="#009B77")

        plt.title(name, y = 1.05, fontdict={'fontsize': 20})

        plt.grid(True, alpha=0.5, ls="-.")
        plt.fill_between(x, y,  0,
                         color="#009B77",
                         alpha=0.2)

        #plt.tight_layout()
        plt.show()
