from py2neo import Graph, Node, Relationship, cypher, Path
import neo4j


class Neo4j():
    graph = None

    def __init__(self):
        print("create neo4j class ...")

    def connectDB(self):
        self.graph = Graph("http://localhost:7474", username="neo4j", password="zzxxxx520")

    def matchsearchItembyTitle(self, value):

        #sql = "MATCH (n:Item { title: " + str(value) + " }) return n;"

        answer = []
        # 是否为类别
        try:
            sql = "MATCH(n:GenreItem{gname: " + str(value) + " }) RETURN  n"
            answer = self.graph.run(sql).data()
        except:
            pass
        # 是否为电影
        if not answer:
            try:
                sql = "MATCH(n:MovieItem{title: " + str(value) + " }) RETURN  n"
                answer = self.graph.run(sql).data()
            except:
                pass
        #是否为人物
        if not answer:
            try:
                sql = "MATCH(n:PersonItem{name: " + str(value) + " }) RETURN  n"
                answer = self.graph.run(sql).data()
            except:
                pass
        return answer

    # def matchItembyTitle(self, value):
    #
    #     #sql = "MATCH (n:Item { title: " + str(value) + " }) return n;"
    #     sql = "MATCH(n:GenreItem{gname: " + str(value) + " })-[r:Genre2Movie]-(q) RETURN  q.title"
    #     answer = None
    #     try:
    #         answer = self.graph.run(sql).data()
    #     except:
    #         print(sql)
    #     return answer

    # def matchGenreItembyTitle(self, value):
    #
    #     #sql = "MATCH (n:GenreItem { title: " + str(value) + " }) return n;"
    #     sql = "MATCH(n:GenreItem{gname: "+str(value)+" })-[r:Genre2Movie]-(q) RETURN  q.title"
    #     answer = None
    #     try:
    #         answer = self.graph.run(sql).data()
    #     except:
    #         print(sql)
    #     return answer

    # 根据title值返回百科MovieItem
    def matchItembyTitle(self, value):
        answer = None
        # 是否为类别
        try:
            sql = "MATCH(n:GenreItem{gname: " + str(value) + " }) RETURN  n"
            answer = self.graph.run(sql).data()
        except:
            pass
        # 是否为电影
        if answer is None:
            try:
                sql = "MATCH(n:MovieItem{title: " + str(value) + " }) RETURN  n"
                answer = self.graph.run(sql).data()
            except:
                pass
        # 是否为人物
        if answer is None:
            try:
                sql = "MATCH(n:PersonItem{name: " + str(value) + " }) RETURN  n"
                answer = self.graph.run(sql).data()
            except:
                pass
        return answer

    # 根据entity的名称返回关系
    def getEntityRelationbyEntity(self, value):

        answer = self.graph.run("MATCH (entity1) - [rel] -> (entity2)  WHERE entity1.name = \"" + str(
                    value) + "\" RETURN entity1,rel,entity2").data()
        ##  要用if not answer , 而不是判断是不是none，因为没有答案就是【】
        if not answer:
            # 关系查询中，如果是movie的查询，只返回电影的演员
            answer = self.graph.run("MATCH (entity1) - [rel:Movie2Person] -> (entity2)  WHERE entity1.title = \"" + str(
                value) + "\" RETURN entity1,rel,entity2").data()
            # answer = self.graph.run("MATCH (n:MovieItem{title:\""+str(value)+"\"})-[rel:Movie2Person]-(entity2)  RETURN n.title,rel.type,entity2.name")
        if not answer:
            answer = self.graph.run("MATCH (entity1) - [rel] -> (entity2)  WHERE entity1.gname = \"" + str(
                value) + "\" RETURN entity1,rel,entity2").data()
        return answer

    # 查找entity1及其对应的关系（与getEntityRelationbyEntity的差别就是返回值不一样）
    def findRelationByEntity(self, entity1):
        answer = self.graph.run("MATCH (n1 {title:\"" + str(entity1) + "\"})- [rel:Movie2Person] -> (n2) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run("MATCH (n1 {name:\"" + str(entity1) + "\"})- [rel:Person2Movie] -> (n2) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run("MATCH (n1 {gname:\"" + str(entity1) + "\"})- [rel:Genre2Movie] -> (n2) RETURN n1,rel,n2").data()

        # if(answer is None):
        # 	answer = self.graph.run("MATCH (n1:PersonItem {title:\""+entity1+"\"})- [rel] -> (n2) RETURN n1,rel,n2" ).data()
        return answer

    # 查找entity2及其对应的关系
    def findRelationByEntity2(self, entity1):
        answer = self.graph.run("MATCH (n1)- [rel:Person2Movie] -> (n2 {title:\"" + str(entity1) + "\"}) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run("MATCH (n1)- [rel:Movie2Person] -> (n2 {name:\"" + str(entity1) + "\"}) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run("MATCH (n1)- [rel] -> (n2 {gname:\"" + str(entity1) + "\"}) RETURN n1,rel,n2").data()

        # if(answer is None):
        # 	answer = self.graph.run("MATCH (n1)- [rel] -> (n2:PersonItem {title:\""+entity1+"\"}) RETURN n1,rel,n2" ).data()
        return answer

    # 根据entity1和关系查找enitty2
    def findOtherEntities(self, entity, relation):
        answer = self.graph.run("MATCH (n1 {title:\"" + str(entity) + "\"})- [rel {type:\"" + str(
            relation) + "\"}] -> (n2) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run("MATCH (n1 {name:\"" + str(entity) + "\"})- [rel {type:\"" + str(
                relation) + "\"}] -> (n2) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run("MATCH (n1 {gname:\"" + str(entity) + "\"})- [rel {type:\"" + str(
                relation) + "\"}] -> (n2) RETURN n1,rel,n2").data()
        # if(answer is None):
        #	answer = self.graph.run("MATCH (n1:PersonItem {title:\"" + entity + "\"})- [rel:RELATION {type:\""+relation+"\"}] -> (n2) RETURN n1,rel,n2" ).data()

        return answer

    # 根据entity2和关系查找enitty1
    def findOtherEntities2(self, entity, relation):
        answer = self.graph.run("MATCH (n1)- [rel {type:\"" + str(relation) + "\"}] -> (n2 {title:\"" + str(
            entity) + "\"}) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run("MATCH (n1)- [rel {type:\"" + str(relation) + "\"}] -> (n2 {name:\"" + str(
                entity) + "\"}) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run("MATCH (n1)- [rel {type:\"" + str(relation) + "\"}] -> (n2 {gname:\"" + str(
                entity) + "\"}) RETURN n1,rel,n2").data()
        # if(answer is None):
        #	answer = self.graph.run("MATCH (n1)- [rel:RELATION {type:\""+relation+"\"}] -> (n2:PersonItem {title:\"" + entity + "\"}) RETURN n1,rel,n2" ).data()

        return answer

    # 根据两个实体查询它们之间的最短路径
    def findRelationByEntities(self, entity1, entity2):
        # answer = self.graph.run("MATCH (p1:PersonItem {name:\"" + str(entity1) + "\"}),(p2:MovieItem{title:\"" + str(
        #     entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN entity1,p,entity2").evaluate()
        # # answer = self.graph.run("MATCH (p1:MovieItem {title:\"" + entity1 + "\"})-[rel:RELATION]-(p2:MovieItem{title:\""+entity2+"\"}) RETURN p1,p2").data()

        # if (answer is None):
        #     answer = self.graph.run(
        #         "MATCH (p1:MovieItem {title:\"" + str(entity1) + "\"}),(p2:PersonItem {name:\"" + str(
        #             entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN entity1,p,entity2").evaluate()
        # if (answer is None):
        #     answer = self.graph.run(
        #         "MATCH (p1:MovieItem {title:\"" + str(entity1) + "\"}),(p2:GenreItem{gname:\"" + str(
        #             entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN entity1,p,entity2").evaluate()
        # if (answer is None):
        #     answer = self.graph.run(
        #         "MATCH (p1:GenreItem {gname:\"" + str(entity1) + "\"}),(p2:MovieItem {title:\"" + str(
        #             entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN entity1,p,entity2").evaluate()

        answer = self.graph.data("MATCH (n1:MovieItem {title:\"" + entity1 + "\"})- [rel] -> (n2:PersonItem{name:\""+entity2+"\"}) RETURN n1,rel,n2" )
        if not answer:
        	answer = self.graph.data("MATCH (n1:PersonItem {name:\"" + entity1 + "\"})- [rel] -> (n2:MovieItem{title:\""+entity2+"\"}) RETURN n1,rel,n2" )
        if not answer:
        	answer = self.graph.data("MATCH (n1:GenreItem {gname:\"" + entity1 + "\"})- [rel] -> (n2:MovieItem{title:\""+entity2+"\"}) RETURN n1,rel,n2" )
        if not answer:
        	answer = self.graph.data("MATCH (n1:MovieItem {title:\"" + entity1 + "\"})- [rel] -> (n2:GenreItem{gname:\""+entity2+"\"}) RETURN n1,rel,n2" )

        relationDict = []
        if not answer:
            for x in answer:
                tmp = {}
                start_node = x.start_node
                end_node = x.end_node
                tmp['n1'] = start_node
                tmp['n2'] = end_node
                tmp['rel'] = x
                relationDict.append(tmp)
        return relationDict

    # 查询数据库中是否有对应的实体-关系匹配
    def findEntityRelation(self, entity1, relation, entity2):
        answer = self.graph.run("MATCH (n1:MovieItem {title:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
            relation) + "\"}] -> (n2:PersonItem{name:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run(
                "MATCH (n1:PersonItem {name:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
                    relation) + "\"}] -> (n2:MovieItem{title:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run(
                "MATCH (n1:GenreItem {gname:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
                    relation) + "\"}] -> (n2:MovieItem{title:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()
        if not answer:
            answer = self.graph.run(
                "MATCH (n1:MovieItem {title:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
                    relation) + "\"}] -> (n2:GenreItem{gname:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()

        return answer

