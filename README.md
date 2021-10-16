# MovieGraph
Film Question Answering System Based on Knowledge Graph (Naive Bayes) 

## 环境配置
🍇1、前期环境配置：包括neo4j等（mac为例）
见：https://blog.csdn.net/Trance95/article/details/119682522

🍇2、requirements（pip install）Cancel changes
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
