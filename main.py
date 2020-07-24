import pandas as pd
from sklearn.metrics import accuracy_score as acc
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('winequality-red.csv',sep=";")

#Correlations between each features and the quality of the wine
corelation = data.corr()['quality'].drop('quality')
print(corelation)

#Heatmap representine detailed diagram of co-relation
sns.heatmap(data.corr())
plt.show()

#Is there any null values in any column in data
print(pd.isnull(data).sum())

#Get only those features whose correlation is graeter than minimum value defined
def get_attributes(min_val):
    return corelation.abs()[corelation.abs()>min_val].index.values.tolist()

features = get_attributes(0.05)
print(features)

x = data[features]
y = data['quality']

#Splitting training and testing data
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=3)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#Models

#Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB as gnb

gaussian = gnb()
gaussian.fit(x_train,y_train)
y_pred = gaussian.predict(x_test)
acc_gn = round(acc(y_pred,y_test)*100,2)
print(acc_gn)

#Decision Tree
from sklearn.tree import DecisionTreeClassifier

dt= DecisionTreeClassifier()
dt.fit(x_train,y_train)
y_pred = dt.predict(x_test)
acc_dt = round(acc(y_pred,y_test)*100,2)
print(acc_dt)

#Random Forest
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
rfc.fit(x_train,y_train)
y_pred = rfc.predict(x_test)
acc_rfc = round(acc(y_pred,y_test)*100,2)
print(acc_rfc)

models = pd.DataFrame({'Model':['Naive Bayes','Decision Tree','Random Forest'],'Score':[acc_gn,acc_dt,acc_rfc]})
models.sort_values(by='Score',ascending=False)

print(models)