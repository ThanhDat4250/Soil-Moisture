import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = pd.read_csv() # insert directory to csv file which stores samples moisture and ADC
data

df = pd.DataFrame(data)
df.describe()

x= df["ADC"].values.reshape(-1,1)
y = df["Moisture"].values.reshape(-1,1)

x_train,x_test, y_train, y_test = train_test_split(x,y, test_size=0.4, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

plt.scatter(x_test,y_test, color='blue', label='All Data Points')
plt.plot(x_test,y_pred, color='red', label='Linear Regression Line')

plt.xlabel('Sensor Value(ADC)')
plt.ylabel('Moisture(%)')
plt.title('Linear Regression: Sensor Value vs Moisture')
plt.legend()

plt.grid()
plt.show()
