import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# import sklearn.linear_model

if __name__ == '__main__':
    iowa_file_path = 'D:/dump/train.csv'

    home_data = pd.read_csv(iowa_file_path)
    # print(home_data.columns)
    print(home_data.shape)
    y = home_data.SalePrice
    # Create the list of features below
    feature_names = ['LotArea'
        , 'YearBuilt'
        , '1stFlrSF'
        , '2ndFlrSF'
        , 'FullBath'
        , 'BedroomAbvGr'
        , 'TotRmsAbvGrd']

    # Select data corresponding to features in feature_names
    X = home_data[feature_names]
    X.dropna()
    # Review data
    # print description or statistics from X
    print(X.describe())

    # print the top few lines
    # print(_)
    print(X.head())
    # specify the model.
    # For model reproducibility, set a numeric value for random_state when specifying the model
    iowa_model = DecisionTreeRegressor(random_state=1)

    # Fit the model
    iowa_model.fit(X, y)

    predictions = iowa_model.predict(X)
    print(predictions)

    """
    Use the head method to compare the top few predictions to the actual home values (in y) 
                for those same homes. Anything surprising?
    """
# Python (>= 3.9)
# NumPy (>= 1.19.5)
# SciPy (>= 1.6.0)
# joblib (>= 1.2.0)
# threadpoolctl (>= 3.1.0)
