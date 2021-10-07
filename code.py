from typing import ClassVar
import plotly.figure_factory as pfffffffffffffffffffffffffff
import csv
import pandas as bear

choose = str(input("Height (h) OR Weight (w): "))

df = bear.read_csv("data.csv")

if (choose == "h"):
    fig = pfffffffffffffffffffffffffff.create_distplot([df["Height(Inches)"].tolist()],["abc"])
    fig.show()
elif (choose == "w"):
    fig = pfffffffffffffffffffffffffff.create_distplot([df["Weight(Pounds)"].tolist()],["abc"])
    fig.show()


