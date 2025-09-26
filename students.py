import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('students.csv')
print(df.head(3))
plt.hist(df['marks'], bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.title('Distribution of Student Marks')
plt.show()
print("Minimum Marks:", df['marks'].min())
print("Maximum Marks:", df['marks'].max())
