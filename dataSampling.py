import csv
import plotly.figure_factory as ff
import pandas as pd
import random


import statistics




df = pd.read_csv("datafile.csv")  # <--- chnage datafile name here(if your csv file has confilcting name 


data = df["reading_time"].tolist()



fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
fig.show()


print("population mean:- ",statistics.mean(data))
def randomMean(counter):
    dataset = []
    for i in range(0, counter):
        randIndex= random.randint(0,len(data))
        value = data[randIndex]
        dataset.append(value)
    
    
    mean = statistics.mean(dataset)
    return mean

def graph(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= randomMean(10)
        mean_list.append(set_of_means)
    graph(mean_list)
    print("sampling mean:- ", statistics.mean(mean_list))
setup()
