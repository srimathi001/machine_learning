import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error

data = pd.read_csv('HousePricePrediction.xlsx - Sheet1 (1).csv')
imputer = SimpleImputer(strategy='mean')
data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
data_encoded = pd.get_dummies(data_imputed)
X = data_encoded.drop(columns=['SalePrice'])
y = data_encoded['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
new_data = np.array([[2500, 4, 3, 2, 3000]])
predicted_price = model.predict(new_data)
print("Predicted price for the new house:", predicted_price[0])
