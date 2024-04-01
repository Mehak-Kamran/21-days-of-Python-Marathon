#Predicting iphone prices using machine learning (MiniProject)
#install pandas-- install pip pandas
#import pandas
import pandas as pd
#read csv file using pandas
stream=pd.read_csv("PredictiphonepriceusingML/iphone_price.csv")
print(stream.head())#it will give top 5 and not all list

#I want to visulize this data to see more clear picture so installing matplotlib
#matplotlib basically draws charts
import matplotlib.pyplot as plt
plt.scatter(stream["version"],stream["price"])
plt.show()
#scikit-learn install cause i want to implement linear regression
from sklearn.linear_model import LinearRegression
#creat model
model=LinearRegression()
#fit data into model, this data is 2d
model.fit(stream[["version"]],stream["price"])
var=int(input("Enter version to predict: "))
#let model predict
pred_pri=model.predict([[var]])

print("IPhone",var,"will be ", pred_pri[0],"in price")
