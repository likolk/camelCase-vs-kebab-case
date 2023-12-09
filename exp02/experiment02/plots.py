import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = [
    {
        'age': 23,
        'comments': 'Kelvin Likollari',
        'questions': 'Looking forward to Christmas,Università della Svizzera italiana,i have no idea,i am a student,eat lunch at mensa,This is a sentence,experimentation and evaluation course,I am a university student,I am from Greece,tomorrow it is gonna be rainy',
        'answers': 'lookingForwardToChristmas,universitàDellaSvizzeraItaliana,iHaveNoIdea,i-am-a-student,eat-lunch-at-mensa,this-is-a-sentence,experimentation-and-evaluation-course,iAmAUniversityStudent,i-am-from-greece,tomorrowItIsGonnaBeRainy',
        'time_taken': '7.174, 1.64, 2.121, 1.859, 1.912, 1.307, 2.25, 1.607, 1.173, 2.093',
        'experience': 'yes'
    },
    {
        'age': 23,
        'comments': 'kelvin test 2',
        'questions': 'tomorrow it is gonna be rainy,eat lunch at mensa,i am a student,I am from Greece,experimentation and evaluation course,Università della Svizzera italiana,i have no idea,Looking forward to Christmas,I am a university student,This is a sentence',
        'answers': 'tomorrowItIsGonnaBeRainy,eat-lunch-at-mensa,i-am-a-student,i-am-from-greece,experimentation-and-evaluation-course,universitàDellaSvizzeraItaliana,iHaveNoIdea,lookingForwardToChristmas,iAmAUniversityStudent,this-is-a-sentence',
        'time_taken': '1.838, 2.123, 1.097, 3.559, 3.156, 2.267, 1.33, 2.694, 2.604, 1.838',
        'experience': 'no'
    }
]

df = pd.DataFrame(data)
df['time_taken'] = df['time_taken'].apply(lambda x: list(map(float, x.split(','))))
df['answers'] = df['answers'].apply(lambda x: x.split(','))
df['questions'] = df['questions'].apply(lambda x: x.split(','))
df = df.explode('time_taken').explode('answers').explode('questions')


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='age', y='time_taken', hue='experience', palette='viridis', s=100)
plt.title('Age vs. Time Taken with Programming Experience')
plt.xlabel('Age')
plt.ylabel('Time Taken')
plt.legend(title='Experience')
plt.grid(True)


plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='experience', y='time_taken', palette='Set3')
plt.title('Programming Experience vs. Time Taken')
plt.xlabel('Experience')
plt.ylabel('Time Taken')
plt.figure(figsize=(8, 6))
sns.histplot(df['time_taken'], bins=10, kde=True)
plt.title('Histogram of Time Taken')
plt.xlabel('Time Taken')
plt.ylabel('Frequency')
plt.grid(True)


def calculate_ecdf(ecdfData):
    n = len(ecdfData)
    x = np.sort(ecdfData)
    y = np.arange(1, n+1) / n
    return x, y




plt.figure(figsize=(8, 6))
x, y = calculate_ecdf(df['time_taken'])
plt.plot(x, y, marker='.', linestyle='none')
plt.title('ECDF of Time Taken')
plt.xlabel('Time Taken')
plt.ylabel('ECDF')
plt.grid(True)
plt.show()