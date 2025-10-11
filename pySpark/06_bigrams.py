from init_spark import ss, sc

"""
PySpark Bigram 计数示例
功能：统计文本中相邻两个词（bigram）出现的频率

步骤：
1. 读取文本文件 data.txt
2. 对每一行进行分词，生成单词列表
3. 生成所有的相邻词对 (bigram)，并为每个 bigram 计数为 1
4. 按 bigram 进行汇总统计（reduceByKey）
5. 打印每个 bigram 及其出现次数
"""
if __name__ == '__main__':
    try:
        lines = sc.textFile("../data/words.txt")  # 返回一个 RDD，每个元素是一行文本

        # 打印原始读取的行（调试用，可选）
        print("=== 原始文本行 ===")
        for line in lines.collect():  # collect() 将 RDD 数据拉取到 Driver，返回 list
            print(line)

        # 3. 对每一行进行分词，生成单词列表
        # map: 每行字符串 -> 单词列表，如 "a b c" -> ["a", "b", "c"]
        words_per_line = lines.map(lambda s: s.split(" "))

        # 4. 生成所有的相邻词对 (bigram)，并为每个 bigram 计数为 1
        # flatMap: 对每个单词列表，生成连续的 (word_i, word_{i+1}) 对
        bigrams = words_per_line.flatMap(
            lambda words: [  # 对每个句子的单词列表
                ((words[i], words[i + 1]), 1)  # 生成一个元组：((word1, word2), 1)
                for i in range(len(words) - 1)  # 遍历所有相邻的词对
            ]
        )

        # 打印生成的 bigram 列表（调试用，可选）
        print("\n=== 生成的 Bigram 列表 ===")
        for bg in bigrams.collect():
            print(bg)

        # 5. 按 bigram 进行汇总，统计每个 bigram 出现的总次数
        # reduceByKey: 对相同的 key（即相同的 bigram），将它们的值（1）相加
        bigram_counts = bigrams.reduceByKey(lambda x, y: x + y)

        # 打印统计结果
        print("\n=== Bigram 出现次数统计结果 ===")
        for (bigram, count) in bigram_counts.collect():
            print(f"{bigram}: {count}")

    finally:
        # 6. 确保 SparkContext 被正确关闭
        sc.stop()
