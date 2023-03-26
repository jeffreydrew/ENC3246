# modules for dataframe and database management, and data visualization
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# ------------------------------------------------------------
#              Question Response Enumerations
# ------------------------------------------------------------

# You live on campus or off campus?
q1 = {1: "On Campus", 2: "Off Campus"}

# For on campus students, how often do you drive
q2 = {
    1: "a few times all semester",
    2: "1-3 times a month",
    3: "3-5 times a month",
    4: "5-10 times a month",
    5: "almost every day",
}

# What parking decal do you have?
q3 = {
    1: "Red 3",
    2: "Red 1",
    3: "Park & Ride",
    4: "Brown 2",
    5: "Brown 3",
}

# How often do you drive to campus each week?
q4 = {1: "0 times", 2: "1-2 times", 3: "3-5 times", 4: "5+ times"}

# When you look for parking, how long do you spend on average?
q5 = {
    1: "Less than 10 minutes",
    2: "10-20 minutes",
    3: "20-30 minutes",
    4: "over 30 minutes",
}

# How many garages do you visit on average before you find an empty parking spot?
q6 = {
    1: "The first one always has an opening",
    2: "1-2 garages",
    3: "More than 2 garages",
}

# How much do you agree with this statement: being able to see which parking spots are open on a floor would save you time.
q7 = {
    1: "Strongly Agree",
    2: "Agree",
    3: "Neutral",
    4: "Disagree",
    5: "Strongly Disagree",
}

# ------------------------------------------------------------
#              Database and Dataframe Management
# ------------------------------------------------------------

conn = sqlite3.connect("responses.db")
c = conn.cursor()


def create_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS responses(q1 TEXT, q2 TEXT, q3 TEXT, q4 TEXT, q5 TEXT, q6 TEXT, q7 TEXT)"
    )
    conn.commit()

def drop_table():
    c.execute("DROP TABLE responses")
    conn.commit()

# this creates a dataframe from the data in responses.db, so that a connection to the database is not required
def read_table():
    df = pd.read_sql_query("SELECT * FROM responses", conn)
    return df


# DANGER ZONE: SINGLE USE METHODS
# closes connection to database
def close():
    conn.close()


# Reponse object for database entries and organization
class Response:
    def __init__(self, q1, q2, q3, q4, q5, q6, q7):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7

    # set q1 to q7 to the corresponding response enumeration
    def insert(self):
        c.execute(
            "INSERT INTO responses (q1, q2, q3, q4, q5, q6, q7) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                q1[self.q1],
                q2[self.q2],
                q3[self.q3],
                q4[self.q4],
                q5[self.q5],
                q6[self.q6],
                q7[self.q7],
            ),
        )
        conn.commit()

class DataAnalyst:
    def __init__(self, df):
        self.df = df

    def pie_chart(self, col):
        # create a pie chart for the columns in the dataframe
        self.df[col].value_counts().plot.pie(autopct="%1.1f%%")
        plt.show()
