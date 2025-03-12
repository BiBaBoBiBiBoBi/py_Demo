import pandas as pd
import sklearn as sk
import sklearn.metrics as skm

"""
随机森林使用许多树，它通过平均每个组成树的预测来进行预测。它通常比单个决策树具有更好的预测准确性，并且可以很好地使用默认参数。如果你继续建模，你可以学习更多的模型，甚至更好的性能，但其中许多是敏感的获得正确的参数。
"""


def learn_demo():
    # Load data
    melbourne_file_path = 'D:/dump/melb_data.csv'
    # iowa_file_path = 'D:/dump/train.csv'

    melbourne_data = pd.read_csv(melbourne_file_path)
    #  Filter rows with missing price values
    filtered_melbourne_data = melbourne_data.dropna(axis=0)  # 0 row  ,1 column
    # Choose target and features
    y = filtered_melbourne_data.Price
    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea',
                          'YearBuilt', 'Lattitude', 'Longtitude']
    X = filtered_melbourne_data[melbourne_features]

    train_X, val_X, train_y, val_y = sk.model_selection.train_test_split(X, y, random_state=0)

    print("create a random tree...")
    forest_model = sk.ensemble.RandomForestRegressor()
    forest_model.fit(train_X, train_y)
    melb_preds = forest_model.predict(val_X)
    print("standard mae : {}".format(skm.mean_absolute_error(val_y, melb_preds)))


def use_tree_predict(train_X, val_X, train_y, val_y):
    # Specify Model
    iowa_model = sk.tree.DecisionTreeRegressor(random_state=1)
    # Fit Model
    iowa_model.fit(train_X, train_y)

    # Make validation predictions and calculate mean absolute error
    val_predictions = iowa_model.predict(val_X)
    val_mae = skm.mean_absolute_error(val_predictions, val_y)
    """
    ,：表示在数字中使用千位分隔符（即每三位数字之间插入一个逗号）
    .：表示小数点的开始。
    0：表示小数点后保留的位数，这里是 0 位，意味着不显示小数部分。
    f：表示格式化为浮点数。
    """
    print("DecisionTree Validation MAE when not specifying max_leaf_nodes: {:,.0f}".format(val_mae))

    # Using best value for max_leaf_nodes
    iowa_model = sk.tree.DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
    iowa_model.fit(train_X, train_y)
    val_predictions = iowa_model.predict(val_X)
    val_mae = skm.mean_absolute_error(val_predictions, val_y)
    print("DecisionTree Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae))


if __name__ == '__main__':
    """
    用train的模型预测test
    """
    iowa_file_path = 'D:/dump/train.csv'
    home_data = pd.read_csv(iowa_file_path)
    # print("HERE IS THE COLUMN OF TRAIN DATA FRAME...")
    # print(home_data.columns)

    full_col_list = home_data.columns.values.tolist()
    full_col_list.remove('SalePrice')
    full_col_list.remove('Id')
    print("FULL COLUMN :{}".format(full_col_list))
    # Create the list of features below
    feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

    # Select data corresponding to features in feature_names
    X = home_data[feature_names]
    y = home_data.SalePrice

    train_X, val_X, train_y, val_y = sk.model_selection.train_test_split(X, y, random_state=1)
    use_tree_predict(train_X, val_X, train_y, val_y)

    # Define a random forest model
    # rf_model = sk.ensemble.RandomForestRegressor(random_state=1)
    # rf_model.fit(train_X, train_y)
    # rf_val_predictions = rf_model.predict(val_X)
    # rf_val_mae = skm.mean_absolute_error(rf_val_predictions, val_y)
    # print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))

    # To improve accuracy, create a new Random Forest model which you will train on all training data
    rf_model_on_full_data = sk.ensemble.RandomForestRegressor()

    # fit rf_model_on_full_data on all data from the training data
    rf_model_on_full_data.fit(X, y)

    # path to file you will use for predictions
    test_data_path = 'D:/dump/test.csv'
    # read test data file using pandas
    test_data = pd.read_csv(test_data_path)
    # print("HERE IS THE COLUMN OF TEST DATA FRAME...")
    # print(test_data.columns)
    # create test_X which comes from test_data but includes only the columns you used for prediction.
    # The list of columns is stored in a variable called features
    test_X = test_data[feature_names]

    # make predictions which we will submit.
    test_preds = rf_model_on_full_data.predict(test_X)
    # print(test_preds)

    """
    运行下面的代码单元格以生成包含您的预测的CSV文件，您可以使用该文件提交给比赛。
    """
    # output = pd.DataFrame({'Id': test_data.Id,'SalePrice': test_preds})
    # output.to_csv('D:/dump/submission2.csv', index=False)
    # learn_demo()
