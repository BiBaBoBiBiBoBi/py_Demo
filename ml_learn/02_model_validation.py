import pandas as pd
import sklearn as sk
# from sklearn.tree import DecisionTreeRegressor
"""
DecisionTreeRegressor
@train_test_split
@mean_absolute_error
@
"""

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    """
    max_leaf_nodes
    使用for循环来比较使用不同max_leaf_nodes值构建的模型的准确性。
    """
    model = sk.tree.DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = sk.metrics.mean_absolute_error(val_y, preds_val)
    return mae


def run_without_any_modify(X, y):
    # Define model
    melbourne_model1 = sk.tree.DecisionTreeRegressor()
    # Fit model
    melbourne_model1.fit(X, y)
    predicted_home_prices = melbourne_model1.predict(X)
    sk.metrics.mean_absolute_error(y, predicted_home_prices)


def run_with_seprate_dataSet(train_X, val_X, train_y, val_y):
    # Define model
    melbourne_model2 = sk.tree.DecisionTreeRegressor()
    # Fit model
    melbourne_model2.fit(train_X, train_y)

    # get predicted prices on validation data
    val_predictions = melbourne_model2.predict(val_X)
    print(sk.metrics.mean_absolute_error(val_y, val_predictions))


def run_with_control_of_leaf_num(train_X, val_X, train_y, val_y):
    for max_leaf_nodes in [5, 50, 500, 5000]:
        my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
        print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" % (max_leaf_nodes, my_mae))

    scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in [5, 50, 500, 5000]}
    best_tree_size = min(scores,key=scores.get) #key 函数会在比较过程中被调用，返回的值将用于确定最小值  // 这是一个可选参数，允许您指定一个函数，该函数用于从 iterable 的每个元素中提取用于比较的值
    print("Best tree size: %d" % best_tree_size)

if __name__ == '__main__':
    # Load data
    melbourne_file_path = 'D:/dump/melb_data.csv'
    melbourne_data = pd.read_csv(melbourne_file_path)
    #  Filter rows with missing price values
    filtered_melbourne_data = melbourne_data.dropna(axis=0)
    # Choose target and features
    y = filtered_melbourne_data.Price
    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea',
                          'YearBuilt', 'Lattitude', 'Longtitude']
    X = filtered_melbourne_data[melbourne_features]

    """
    1 直接建模，用模型的训练数据去预测模型
    """
    run_without_any_modify(X, y)

    """
    2 由于模型的实用价值来自于对新数据的预测，因此我们对未用于构建模型的数据进行性能评估。
    最直接的方法是从模型构建过程中排除一些数据，
    然后使用这些数据来测试模型在以前没有见过的数据上的准确性。此数据称为验证数据。
    """
    # split data into training and validation data, for both features and target
    # The split is based on a random number generator. Supplying a numeric value to
    # the random_state argument guarantees we get the same split every time we
    # run this script.
    # from sklearn.model_selection import train_test_split
    train_X, val_X, train_y, val_y = sk.model_selection.train_test_split(X, y, random_state=0)
    run_with_seprate_dataSet(train_X, val_X, train_y, val_y)

    """
    3 有几个控制树深度的替代方案，许多方案允许通过树的某些路由具有比其他路由更大的深度。但是max_leaf_nodes参数提供了一种非常明智的方法来控制过拟合和欠拟合。
    我们允许模型生成的叶子越多，我们从上图中的欠拟合区域移动到过拟合区域的距离就越大。
    
    过度拟合：捕捉未来不会重现的虚假模式，导致预测不太准确，或
    拟合不足：未能捕捉相关模式，再次导致预测不太准确。
    """
    # compare MAE with differing values of max_leaf_nodes
    run_with_control_of_leaf_num(train_X, val_X, train_y, val_y)
