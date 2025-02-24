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

#Making Rank a Column
university.reset_index(inplace=True)

#Plot of Top 200 Universities by Ranking
plt.figure(figsize=(75, 50))
plt.scatter(university['Rank'], university['Name'], color='skyblue', s=100)
plt.title("Top 200 Universities in North America by Rank", fontsize=20)
plt.xlabel("Rank", fontsize=15)
plt.ylabel("University", fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=10)
plt.grid(axis='x', linestyle='--', alpha=0.7)

#Saving the Plot
plt.tight_layout()
plt.savefig("charts/UniversityRank.png")
plt.show()
