import cnsyn

# 查询同义词（全部词库）
word = "垃圾"
cnsyn.search(word)
cnsyn.search(word, topK=3)
# 使用wiki词库
cnsyn.search(word, origin="wiki")
# 使用中文同义词字典库
cnsyn.search(word, origin="cndict")

# 基于向量的语义召回Approximate Nearest Neighbor Search
l = cnsyn.anns(word)
print(l)
cnsyn.anns(word, topK=3)
