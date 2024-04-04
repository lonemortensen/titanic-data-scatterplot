# =======================================================================
# Project: Titanic Dataset
# Description: Displaying Titanic datasets.
# The project uses Python's Pandas, Matplotlib, and Seaborn libraries to visualize the Titanic datasets. The result is a scatterplot comparing both age and passenger fare data with those who survived the Titanic.
# Background: Coursework for Skillcrush's "Preparing & Displaying Data with Python" class.

# ==== *** ====

# The main.py file contains code that:
# - reads data from a csv file and stores the data in a Pandas dataframe.
# - replaces and clarifies column values in the dataframe for use in the
# scatterplot's legend.
# - uses Seaborn to create a scatterplot.
# =======================================================================

import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Stores data in a Pandas dataframe and holds the Titanic data and the scatterplot legend, using the replace() function to clarify legend values based on the "Survived" column:
dataframe = pd.read_csv("titanic.csv", delimiter=",")
dataframe = dataframe.replace(
  {"Survived": {
    0: "Did not survive",
    1: "Survived"
  }})

# Builds Seaborn scatterplot comparing data on age and fare with those who survived:
sns.scatterplot(x="Age", y="Fare", hue="Survived", data=dataframe)

plt.xlabel("Passenger Age")
plt.ylabel("Passenger Fare")

plt.savefig("titanic.png")
