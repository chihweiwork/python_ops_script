import pandas as pd
import datetime
import pdb
import hvplot
import hvplot.pandas
import holoviews as hv
from bokeh.models.formatters import DatetimeTickFormatter

def count_time_range(stime, etime, row):
    count = 0
    data = row.to_dict()
    for x in datetime_range(stime, etime, datetime.timedelta(minutes=1)):
        if x >= data['stime'] and x <= data['etime']:
            count += 1

    return count

def myplot(data):
    return data.hvplot() * data.hvplot.scatter()

def new_count_time_range(stime, etime, data):
    
    output = {
        "time":[], "count":[]
    }
    for t in datetime_range(stime, etime, datetime.timedelta(minutes=1)):
        output['time'].append(t)
        output['count'].append(
            len(data.loc[(data['stime'] <= t) & (data['etime'] >= t)])
        )

    return pd.DataFrame(output)

def datetime_range(stime, etime, deltaT):

    while stime <= etime:
        stime += deltaT
        yield stime

def to_datetime(x):
    return datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":

    data = pd.read_csv("./dummy.csv")

    data['stime'] = data.stime.apply(lambda x: to_datetime(x))
    data['etime'] = data.etime.apply(lambda x: to_datetime(x))

    t1 = data.stime.min()
    t2 = data.etime.max()

    result = new_count_time_range(t1, t2, data)
    formatter = DatetimeTickFormatter(days = '%m/%d', hourmin = '%H:%M')
    #plot = myplot(result)
    plot = result.set_index('time').hvplot(xformatter=formatter)
    #fig = hv.Layout(plot)#.cols(1)
    #hv.save(fig, "./result.html")
    hvplot.save(plot, './result.html')
