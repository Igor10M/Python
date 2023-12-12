import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("50_Startups.csv")

dataset.dropna(inplace = True)

dataset.drop('R&D Spend', axis=1, inplace=True)

print(dataset)

X = dataset.iloc[:, :-1]
Y = dataset.iloc[:, -1]

states = pd.get_dummies(X['State'], drop_first= True)

X = pd.concat([X,states], axis=1)

X = X.drop('State', axis=1)

print(X)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

from sklearn.linear_model import LinearRegression

model =LinearRegression()

model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

print(model.predict(np.array([80000,120000,0,1]).reshape(1,-1)))

from sklearn.metrics import r2_score

Score = r2_score(Y_test,Y_pred)

print(Score)

plt.scatter(Y_test,Y_pred, color = 'red')
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='blue', linestyle='--')
plt.show()s