'''
1 确认dp[i]数组含义
2 递推公式
3 初始化数组
4 遍历顺序
5 打印动态数组
'''


# 斐波那契数列
def calculate_fin(n):
    if n == 1 or n == 0:
        return 1
    else:
        return calculate_fin(n - 1) + calculate_fin(n - 2)


def cal_fin(n):
    dp = [[] for _ in range(0, n + 1)]
    dp[0], dp[1] = 1, 1
    # print(dp)
    if n < 2: return dp[n]
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # print(f"dp[n]={dp[n]}")
    return dp[n]


# 爬n级台阶，有多少种爬法？（每一步可以迈一步或者两步，且仅有这两种方法）
def climb_ladder(n):
    pass
    dp = [[] for _ in range(0, n + 1)]
    '''
    爬1级，只有一种方法；爬两级，有2中方法；
    爬3级，仅有dp[1],dp[2]两种方法（从第二级迈一步/从第一级迈两步）
    爬n级，仅有dp[n-1],dp[n-2]两种方法（从第n-1级迈一步/从第n-2级迈两步）
    '''
    dp[0], dp[1], dp[2] = 0, 1, 2
    if n < 3:
        return dp[n]
    # dp[i] = dp[i-1] + dp[i-2]
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


''' 跳台阶，初始位置可以选择0或1. 到达台阶i 不需要花费i对应的体力，离开台阶i 才需要花费cost[i]
结果要计算走完所有台阶的值，可以理解为走到len(cost)+1的位置需要的体力值

给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。
'''


def climb_ladder_with_min_cost(cost_lst):
    len_of_cost = len(cost_lst)
    # dp[i] : i 第几集台阶，value = 离开下标i的台阶所消耗的最小花费
    dp = [[] for _ in range(0, len_of_cost + 1)]

    dp[0], dp[1] = 0, 0

    for i in range(2, len_of_cost + 1):
        dp[i] = min(dp[i - 1] + cost_lst[i - 1], dp[i - 2] + cost_lst[i - 2])
    return dp[len_of_cost]


'''
⼀个机器⼈位于⼀个 m x n ⽹格的左上⻆ （起始点在下图中标记为 “Start” ）。
机器⼈每次只能向下或者向右移动⼀步。机器⼈试图达到⽹格的右下⻆（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
'''


# 62
def unique_path(row, col):  # col->m , row ->n
    # dp[i][j] :走到(i,j)位置包含的路径数目，它仅有两种情况：
    #       即从本格的上方(i-1,j)，或者本格的左方(i,j-1)过来，所以递推公式为： dp[i][j] = dp[i-1][j] + dp[i][j-1]
    dp = [[[] for _ in range(col)] for _ in range(row)]  # 正确的初始化方式
    for i in range(col):
        dp[0][i] = 1  # 第一列只能竖着走
    for j in range(row):
        dp[j][0] = 1  # 第一行只能横着走

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    # print(dp)
    return dp[row - 1][col - 1]


# 63
def unique_path_ii(obstacleGrid):
    # 极端边界情况：
    row, col = len(obstacleGrid), len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 or obstacleGrid[row - 1][col - 1] == 1:
        return 0

    dp = [[0 for _ in range(col)] for _ in range(row)]  # 正确的初始化方式
    for i in range(col):
        if obstacleGrid[0][i] == 1:  # Obstacles
            break
        else:
            dp[0][i] = 1  # 第一列只能竖着走
    for j in range(row):
        if obstacleGrid[j][0] == 1:  # Obstacles
            break
        else:
            dp[j][0] = 1  # 第一行只能横着走
    # print(dp)

    for i in range(1, row):
        for j in range(1, col):
            if obstacleGrid[i][j] == 1:  # Obstacles
                continue
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp)
    return dp[row - 1][col - 1]


# 3
def longestCommonPrefix(str_lst):
    prefix = str_lst[0]
    len_lst = len(str_lst)
    len_pref = len(prefix)
    for word in range(1, len_lst):
        while prefix != word[0:len_pref]:
            len_pref -= 1
            if len_pref == 0:
                return ""
            prefix = prefix[0:len_pref]
    return prefix


# 96
def numTrees(n):
    '''
    二叉搜索树的左子树所有节点一定比根节点小，右子树所有节点一定比根节点大
    空树也算一种二叉搜索树
    '''
    # define a dp[i] list,which i means the number of nodes in this tree;dp[i] means the number of condition these nodes can construct a tree
    dp = [0 for _ in range(n + 1)]
    # init this lst
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):  # 2
        for j in range(1, i + 1):  # 1
            dp[i] += dp[j - 1] * dp[i - j]
    return dp[n]


# 343 key 拆分m个近似相同的数字
def integer_break(n):  # n->[2,58]
    pass
    dp = [0 for _ in range(n + 1)]
    dp[0], dp[1], dp[2] = 0, 1, 1

    for i in range(3, n + 1):
        for j in range(1, i):
            '''在遍历所有可能的分解方式时，需要保留之前已经计算出的最大值。
            dp[i] 表示整数 i 分解为至少两个正整数后的 最大乘积。
            在遍历 a（分解出的第一个数）的过程中，我们需要 不断更新 dp[i]，确保它能记录下所有可能分解方式中的最大值。
            '''
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    return dp[n]


def sort_string(s):
    str_need_tobe_sorted = ''
    for char in s:
        if char.isalpha():
            str_need_tobe_sorted += char
    sorted_str = sorted(str_need_tobe_sorted, key=str.upper)
    ind = 0
    res_str = ''
    for i in range(len(s)):
        if s[i].isalpha():
            res_str += sorted_str[ind]
            ind += 1
        else:
            res_str += s[i]
    return res_str


def max_unrepeated_str(s):
    leng = len(s)
    if leng < 2: return s
    indicator = 0
    max_str = tmp_str = ''
    for i in range(0, leng):
        while s[i] in tmp_str:
            indicator += 1
            tmp_str = s[indicator:i]
        tmp_str += s[i]
        max_str = tmp_str if len(tmp_str) >= len(max_str) else max_str
    return max_str


if __name__ == '__main__':
    n = 5
    s = "au"
    # print(calculate_fin(n))
    # print(cal_fin(n))
    # print(climb_ladder(n))
    # print(climb_ladder_with_min_cost([1,100,1,1,1,100,1,1,100,1]) )  # 6
    # print(unique_path(3, 7))  # 28
    # print(unique_path_ii([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    # print(numTrees(3))
    # print(sort_string('Hello NowCoder!'))
    print(max_unrepeated_str(s))
