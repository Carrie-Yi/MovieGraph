# MovieGraph
Film Question Answering System Based on Knowledge Graph (Naive Bayes) 
见：https://blog.csdn.net/Trance95/article/details/119613713
![image](https://user-images.githubusercontent.com/57583392/137582740-af4e5583-edc6-4fbf-8bfe-5b46e5429f98.png)
![image](https://user-images.githubusercontent.com/57583392/137582748-4018438e-af7f-4c2a-807c-f3eaea85acc1.png)
![image](https://user-images.githubusercontent.com/57583392/137582750-79fa3280-7c97-43c2-a14a-f11e9dab0675.png)

## 环境配置
🍇1、前期环境配置：包括neo4j等（mac为例）

见：https://blog.csdn.net/Trance95/article/details/119682522

🍇2、requirements（pip install）

Cython>=0.28.5

Django>=1.11.7

thulac>=0.1.2

py2neo==4.1.0

pyfasttext==0.4.5

#（如果是mac,  CXX=/usr/bin/clang CC=/usr/bin/clang pip3 install --no-cache pyfasttext）

pinyin>=0.4.0

pymongo>=3.6.1

Neo4j

Neo4j-driver==1.6.2

Requests

🍇3、更改激活环境

Movie_Graph/Movie_KnowledgeGraph/demo/django_server_start.sh

在django_server_start.sh文件中, 更改激活环境为自己使用的环境。

## 数据预处理
见note文件夹
## neo4j数据库建立
见note文件夹
## Hanlp分词以及朴素贝叶斯分类
见note文件夹
