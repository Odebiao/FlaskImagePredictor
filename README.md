# 垃圾分类爬虫模型预测
Python 3.8
Flask 3.0.3
CUDA11.8
CUDNN8.6
tensorflow-gpu==2.10.1
# 执行步骤：
1.scraper.py
获取的图像数量尽可能多一些
2.spilt.py
分割数据集，会保存在新目录split_data
3.model_pre.py
模型训练包含使用CPU和GPU两部分
4.test.py
进行测试
