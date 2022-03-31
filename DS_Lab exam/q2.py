from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  r2_score
dataset=load_boston()
x=dataset.data
y=dataset.target
xts,xtr,yts,ytr=train_test_split(x,y,test_size=0.4,random_state=42)
model=LinearRegression()
model.fit(xtr,ytr)
yp=model.predict(xts)
var=model.score(xts,yp)
print("Prediction: \n",yp)
print("Varience Score: ",var)
print("Coefficient :\n",model.coef_)
print("Intercept: ",model.intercept_)
print(r2_score(yts,yp))
