import logging

# 配置日志，设置日志级别为 INFO，并指定日志格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def word_search(word_list, keyword):
    normalized = [word.rstrip('.,').lower() for word in word_list]
    return keyword.lower() in normalized


if __name__ == '__main__':
    logging.info("程序开始执行。")
    
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    keyword = 'casino'
    import pandas as pd
    keyword_lower = keyword.lower()
    
    logging.info(f"搜索关键词: {keyword_lower}")
    logging.info(f"文档列表: {doc_list}")
    
    for idx, doc in enumerate(doc_list):
        logging.info(f"正在处理文档索引 {idx}: {doc}")
        sub_doc_list = doc.split()
        found = word_search(sub_doc_list, keyword_lower)
        if found:
            logging.info(f"在文档索引 {idx} 中找到关键词 '{keyword_lower}'。")
        else:
            logging.info(f"在文档索引 {idx} 中未找到关键词 '{keyword_lower}'。")
    
    logging.info("程序执行完毕。")



