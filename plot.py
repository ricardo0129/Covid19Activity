import pandas as pd
import numpy as np
import math
import datetime
import matplotlib.pyplot as plt 

def previous_day(day1,change):
    format_str = '%m-%d-%Y'
    datetime_obj = datetime.datetime.strptime(day1, format_str)
    delta = datetime.timedelta(days=change)
    datetime_obj+=delta
    return datetime_obj.strftime('%m-%d-%Y')

def confirmed_day(day,state="all"):
    d = pd.read_csv("./data/"+day+".csv")
    if state=="all":
        total = sum(d["Confirmed"].astype(np.int64))
    else:
        total = sum(d[d["Province_State"]==state]["Confirmed"])
    return total

def confirmed_states(day):
    d = pd.read_csv("./data/"+day+".csv")
    total = d["Confirmed"].astype(np.int64)
    e = pd.read_csv("./data/"+previous_day(day,-1)+".csv")
    total2 = e["Confirmed"].astype(np.int64)
    lat = e["Lat"]
    lon = e["Long_"]
    data = []
    for i in range(len(e)):
        total[i]-=total2[i]

    for i in range(len(total)):
        if not math.isnan(lat[i]):
            data.append([max(total[i],0),lat[i],lon[i]])
    return data


def confirmed_cases_range(day1,day2,state="all"):
    return confirmed_day(day2,state)-confirmed_day(previous_day(day1,-1),state)

def confirmed_cases_day(day,state="all"):
    return confirmed_cases_range(day,day,state)

def get_data(day_from,day_to,state="all"):
    data = []
    while True:
        data.append(confirmed_cases_day(day_from,state))
        if day_from == day_to:
            break
        day_from = previous_day(day_from,1)
    return data

def adjust_7day_avg(data):
    sum = 0 
    for i in range(7):
        sum+=data[i]
        data[i] = sum//(i+1)

    for i in range(7,len(data)):
        sum-=data[i-7]
        sum+=data[i]
        data[i] = sum//7

def add_data(data,label):
    format_str = '%m-%d-%Y'
    #datetime_obj = datetime.datetime.strptime(start_date, format_str)
    plt.ticklabel_format(style='plain')
    #x = [datetime_obj + datetime.timedelta(days=i) for i in range(len(data))]
    # plot
    plt.plot(data,label=label)
    #plt.gcf().autofmt_xdate()

def show_graph():
    plt.legend(loc='upper center')
    plt.xlabel("# of Days")
    plt.ylabel("# of Cases")
    plt.show()

def map_data(day):
    data = confirmed_states(day)
    return data
    # lat, lon, cases

# 2020-08-08 to 2021-02-24
'''
data = get_data("08-08-2020","02-24-2021","Florida")
adjust_7day_avg(data)
add_data(data,"Florida")
data = get_data("08-08-2020","02-24-2021","California")
adjust_7day_avg(data)
add_data(data,"California")
show_graph()
'''