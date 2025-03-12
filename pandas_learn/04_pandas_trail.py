if __name__ == '__main__':
    import pandas as pd

    pd.set_option("display.max_rows", 5)
    # DF
    fruits1 = pd.DataFrame([[30, 30]], columns=['col1', 'col2'])
    # print(fruits1.head(),end='\n\n')
    fruits2 = pd.DataFrame({'apple': [10], 'banana': [20]})
    # print(fruits2.head(),end='\n\n')
    fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'], index=['2017 Sales', '2018 Sales'])
    # print(fruit_sales.head(),end='\n\n')

    #Series
    ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], name='Dinner',
                            index=['Flour', 'Milk', 'Eggs', 'Spam'])

    # CSV
    wine_file_path='D:/dump/winemag-data-130k-v2.csv'
    reviews = pd.read_csv(wine_file_path, index_col=0)
    print(reviews.head(),end='\n\n')
    """
    ## 基于索引的选择 -  iloc (AKA  indexed-loc)
    运算':'本身也来自原生 Python，意思是“一切”。
    但是，当与其他选择器结合使用时，它可以用于指示值的范围。
    """
    # print(reviews.iloc[0]) # 返回第一行
    # print(reviews.iloc[:,0]) # 返回第一列
    # print(reviews.iloc[:3, 0]) # 第一、第二和第三行中选择country列
    print(reviews.iloc[[0, 1, 2], 0]) # 用列表选择  第一、第二和第三行中选择country列
    print(reviews.iloc[1:3, 0]) # 仅选择第二个和第三个条目
    """负数可以用于选择。这将从值的末尾开始向前计数。例如，这里是数据集的最后五个元素。"""
    print(reviews.iloc[-5:])

    """ ## 基于标签的选择  loc"""
    # 要获取reviews中的第一个条目，我们现在需要执行以下操作：
    print(reviews.loc[0, 'country'])

    """
    iloc在概念上比loc更简单，因为它忽略数据集的索引。当我们使用iloc时，我们将数据集视为一个大矩阵（列表的列表），我们必须按位置对其进行索引。相比之下，
    loc使用索引中的信息来完成其工作。由于您的数据集通常具有有意义的索引，因此使用loc执行操作通常更容易。
    例如，下面是使用loc更容易的一个操作：选择如下三列的所有行
    """
    print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

    """
    iloc使用 Python stdlib 索引方案，其中包含范围的第一个元素并排除最后一个元素。因此0:10将选择条目0,...,9 。
    同时， loc包含索引。因此0:10将选择条目0,...,10
    
    loc 可以索引任何 stdlib 类型：例如字符串
    """

    # 条件选择   ampersand (&) ==and ,  pipe(|) == or
    print(reviews.loc[reviews.country == 'Italy'])
    print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])
    print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])
    # isin允许您选择其值“位于”值列表中的数据
    print(reviews.loc[reviews.country.isin(['Italy', 'France'])])
    # isnull ,notnull  这些方法可让您突出显示空（或非空）( NaN ) 的值。
    print(reviews.loc[reviews.price.notnull()])

    """分配数据"""
    # 向df中添加了一个名为 critic的列，其值全部为 everyone
    reviews['critic']= 'everyone'
    # 或者使用可迭代的值： 从len 到0，递减的一列数据
    reviews['index_backwards'] = range(len(reviews), 0, -1)
    print(reviews[['critic', 'index_backwards']])

    # 以下代码返回值相等。iloc 不能处理str,
    # reviews.iloc[:100, [0, 11]] == reviews.loc[:99, ['country', 'variety']]

    print(reviews.iloc[:100, range(3, 11)])

    #SummaryFunction and Maps
    
