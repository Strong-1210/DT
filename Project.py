#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#loading the dataset
df = pd.read_csv('D:\Project\Data-Science-Projects-main\Calgary Crime Data Analysis and Neural Network Model\Community_Crime_Statistics_20240522.csv')
df.head() 

fig, ax = plt.subplots(1, 2, figsize=(15, 5))
#Top 10 Communities with Highest Crime Rate
df['Community'].value_counts().head(10).plot.pie(autopct='%1.1f%%', ax = ax[0])
ax[0].set_title('Top 10 Communities with Highest Crime Rate')
ax[0].set_ylabel('')
#Top 10 Communities with Lowest Crime Rate
df['Community'].value_counts().tail(10).plot.pie(autopct='%1.1f%%', ax = ax[1])
ax[1].set_title('Top 10 Communities with Lowest Crime Rate')
ax[1].set_ylabel('')