'''
INF601 - Programming in Python
Assignment# MiniProject 2
I, Cole Darling, affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

import pandas as pd
import matplotlib.pyplot as plt
import os

#Charts Directory
os.makedirs("charts", exist_ok=True)

university = pd.read_csv("NorthAmericaUniversities.csv", encoding="ISO-8859-1", index_col=0)

#Shape of the DataFrame
print(university.shape)

#Column Names
print(university.columns)

#First Few Rows
print(university.head())

university.plot(kind="bar", x="University", y="Rank")
plt.title("Universities in North America by Rank")
plt.xlabel("University")
plt.ylabel("Rank")
