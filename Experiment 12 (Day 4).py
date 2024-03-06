import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

data = pd.read_csv('carprice.csv')

features = ['Feature1', 'Feature2', 'Feature3', ...]
target = 'Price'

if target not in data.columns:
    exit()

X = data[features]
y = data[target]

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GradientBoostingRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

new_data = pd.DataFrame([[...]])
new_data = pd.get_dummies(new_data)
prediction_new_data = model.predict(new_data)
print("Predicted price for new data:", prediction_new_data)
