from data import *
import random

if __name__ == "__main__":
    drop_table()
    create_table()
    for i in range(127):
        q1res = random.choice(list(q1.keys()))
        q2res = random.choice(list(q2.keys()))
        q3res = random.choice(list(q3.keys()))
        q4res = random.choice(list(q4.keys()))
        q5res = random.choice(list(q5.keys()))
        q6res = random.choice(list(q6.keys()))
        q7res = random.choice(list(q7.keys())[:2])

        r = Response(q1res, q2res, q3res, q4res, q5res, q6res, q7res)

        r.insert()

    # show pie charts of data
    df = read_table()
    da = DataAnalyst(df)
    da.pie_chart("q1")
    da.pie_chart("q2")
    da.pie_chart("q3")
    da.pie_chart("q4")
    da.pie_chart("q5")
    da.pie_chart("q6")
    da.pie_chart("q7")
