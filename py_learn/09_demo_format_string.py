contacts = ["joe", "john"]

# format func for string output:
year = "蛇"
for name in contacts:
    msg_content = """
    吕慧纯碱，心愿朝气。
    心碎复制，夫妻东来。
    金{0}贺岁，欢乐祥瑞。
    金{0}敲门，五福临门。
    给{1}及家人拜年啦！
    新春快乐，{0}年大吉！
    """.format(year, name)
    print(msg_content)

var1 = "snake"
var2 = "lily"
msg_usage_02 = f"""
    金{var1}贺岁，欢乐祥瑞。
    金{var2}敲门，五福临门。
"""
# {number : .nf}  --> to round a float
var_float = 2.458576
print(f"hi, ur score is {var_float:.2f}")
# r"" raw str
print(r" abc /a/n/r/d/s")