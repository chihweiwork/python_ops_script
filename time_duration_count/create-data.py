import pandas as pd
import datetime
import random

def gen_setime():

    stime = random.randrange(0,24,1)
    etime = random.randrange(0,24,1)
    while etime <= stime:
        etime = random.randrange(0,24,1)

    _gen_time = lambda x: random.randrange(0,60,1)
    
    stime = datetime.datetime(
        2022, 1, 17, stime, _gen_time(1), _gen_time(1)
    )

    etime = datetime.datetime(
        2022, 1, 17, etime, _gen_time(1), _gen_time(1)
    )
    #print(stime, etime)
    return (stime, etime)

if __name__ == "__main__":

    data_l = list()
    cols = ("stime", "etime")
    for _ in range(5):
        data_l.append(
            dict(zip(cols, gen_setime()))
        )

    pd.DataFrame(data_l).to_csv("./dummy.csv", index=False)
