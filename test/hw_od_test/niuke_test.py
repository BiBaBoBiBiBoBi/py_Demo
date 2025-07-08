import numpy as np


def solu_16():
    pass
    line_1 = "50 5"
    line_x = ["20 3 5", "20 3 5", "10 3 0", "10 2 0", "10 1 0"]
    # = 130
    budget, purchase_num = map(int, line_1.split())  #
    primary, annex = {}, {}

    for i in range(1, purchase_num + 1):
        v, w, q = map(int, line_x[i - 1].split())
        if q == 0:
            primary[i] = [v, w]
        else:
            if q in annex.keys():
                annex[q].append([v, w])
            else:  # ['5':[[2,3] ,[3,4] ]
                annex[q] = [[v, w]]

    #   budget == j, item_id == i
    # dp = np.full((purchase_num + 1, purchase_num + 1), 0)  # dp[i][j] 代表 从物品 0~i ,在预算j之内获得的最高满意度
    # dp[i][0] = 0 有东西没预算, dp[0][j]=0 没预算有东西
    dp = [0] * (budget + 1)

    print(f"primary : {primary}")
    print(f"annex : {annex}")

    for key in primary.keys():
        w_lst, v_lst = [], []

        w_lst.append(primary[key][0])  # 1:m
        v_lst.append(primary[key][0] * primary[key][1])
        if key in annex.keys():
            a1_w = annex[key][0][0]
            a1_v = annex[key][0][1]
            w_lst.append(w_lst[0] + a1_w)  # 2:m,a1
            v_lst.append(v_lst[0] + a1_w * a1_v)
            if len(annex[key]) > 1:
                a2_w = annex[key][1][0]
                a2_v = annex[key][1][1]
                w_lst.append(w_lst[0] + a2_w)  # 3:m,a2
                v_lst.append(v_lst[0] + a2_w * a2_v)

                w_lst.append(w_lst[0] + a1_w + a2_w)  # 4:m,a1,a2
                v_lst.append(v_lst[0] + a1_w * a1_v + a2_w * a2_v)
        # 所有情况初始化完成，对w_lst,v_lst进行筛选
        # print(f"w:{len(w_lst)} , v:{len(v_lst)}")
        for j in range(budget, -1, -10):
            for k in range(len(w_lst)):
                if j - w_lst[k] >= 0:
                    dp[j] = max(dp[j], dp[j - w_lst[k]] + v_lst[k])

    print(max(dp))


def solu_16_2():
    line_1 = "50 5"
    line_x = ["20 3 5", "20 3 5", "10 3 0", "10 2 0", "10 1 0"]
    # 输入预算和物品数量
    # budget, purchase_num = map(int, input().split())
    budget, purchase_num = map(int, line_1.split())  #

    budget //= 10  # 价格是10的整数倍，降低空间/时间复杂度

    # 初始化价格和重要程度
    prices = [[0] * 3 for _ in range(purchase_num + 1)]
    price_multiply_priority = [[0] * 3 for _ in range(purchase_num + 1)]

    # 输入物品信息
    for i in range(1, purchase_num + 1):
        price, weight, q = map(int, line_x[i - 1].split())
        price //= 10
        weight *= price
        if q == 0:
            prices[i][0] = price
            price_multiply_priority[i][0] = weight
        else:
            if prices[q][1] == 0:
                prices[q][1] = price
                price_multiply_priority[q][1] = weight
            else:
                prices[q][2] = price
                price_multiply_priority[q][2] = weight

    # 初始化动态规划表
    # dp[i][j] 代表 从物品 0~i ,在预算j之内获得的最高满意度
    # dp[i][0] = 0 有东西没预算, dp[0][j]=0 没预算有东西
    dp = [[0] * (budget + 1) for _ in range(purchase_num + 1)]
    # 动态规划填充
    for i in range(1, purchase_num + 1):
        for j in range(1, budget + 1):
            price, weight = prices[i][0], price_multiply_priority[i][0]
            a1_p, a1_w = prices[i][1], price_multiply_priority[i][1]
            a2_p, a2_w = prices[i][2], price_multiply_priority[i][2]

            dp[i][j] = max(dp[i - 1][j - price] + weight, dp[i - 1][j]) if j >= price else dp[i - 1][j]

            dp[i][j] = max(dp[i - 1][j - price - a1_p] + weight + a1_w, dp[i][j]) if j >= (price + a1_p) else dp[i][j]
            dp[i][j] = max(dp[i - 1][j - price - a2_p] + weight + a2_w, dp[i][j]) if j >= (price + a2_p) else dp[i][j]
            dp[i][j] = max(dp[i - 1][j - price - a1_p - a2_p] + weight + a1_w + a2_w, dp[i][j]) if j >= (price + a1_p + a2_p) else dp[i][j]

    # 输出结果
    # print(dp)
    print(dp[purchase_num][budget] * 10)


def solu_33():
    '''input
    10.0.3.193
    167969729
    '''
    ip_lst = list(map(int, input().split(".")))
    bi = bin(int(input())).replace("0b", "")
    bi = (32 - len(bi)) * "0" + bi

    n_list = []
    for i in ip_lst:
        b = bin(i).replace("0b", "")
        length = 8 - len(b)
        b = length * "0" + b
        n_list.append(b)
    print(int("".join(n_list), 2))

    res_lst = [bi[0:8], bi[8:16], bi[16:24], bi[24:32]]
    res_lst = list(map(lambda x: int(x, 2), res_lst))
    print(".".join([str(x) for x in res_lst]))


if __name__ == '__main__':
    pass
    solu_16_2()
