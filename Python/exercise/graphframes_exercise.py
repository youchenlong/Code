from pyspark import SparkConf
from pyspark.sql import SparkSession
from graphframes import GraphFrame
import networkx as nx
import matplotlib.pyplot as plt

conf = SparkConf().setAppName('test').setMaster('local[*]')
spark = SparkSession.builder.getOrCreate()

vertices = spark.createDataFrame([
  ("a", "Alice", 34),
  ("b", "Bob", 36),
  ("c", "Charlie", 30),
  ("d", "David", 29),
  ("e", "Esther", 32),
  ("f", "Fanny", 36),
  ("g", "Gabby", 60)], ["id", "name", "age"])

edges = spark.createDataFrame([
  ("a", "b", "friend"),
  ("b", "c", "follow"),
  ("c", "b", "follow"),
  ("f", "c", "follow"),
  ("e", "f", "follow"),
  ("e", "d", "friend"),
  ("d", "a", "friend"),
  ("a", "e", "friend")
], ["src", "dst", "relationship"])

# 创建图
graph = GraphFrame(vertices, edges)

# 图的保存和加载
# graph.vertices.write.parquet('hdfs://localhost:9000/usr/hadoop/graph/vertices')
# graph.edges.write.parquet('hdfs://localhost:9000/usr/hadoop/graph/edges')
# graph.vertices.write.parquet('file:///home/ycl/Desktop/Code/Python_exercise/graph/vertices')
# graph.edges.write.parquet('file:///home/ycl/Desktop/Code/Python_exercise/graph/edges')
# vertices = spark.read.parquet('file:///home/ycl/Desktop/Code/Python_exercise/graph/vertices')
# edges = spark.read.parquet('file:///home/ycl/Desktop/Code/Python_exercise/graph/edges')
# graph = GraphFrame(vertices, edges)

# 顶点视图，边视图，三元组视图
# graph.vertices.show()
# graph.edges.show()
# graph.triplets.show()

# 模式视图
# motifs = graph.find('(a)-[]->(b);(b)-[]->(c);!(a)-[]->(c)').filter('a.id!=c.id')
# motifs.show()

# 度、入读、出度
# graph.degrees.show()
# graph.inDegrees.show()
# graph.outDegrees.show()


# 网页排名
# results = graph.pageRank(resetProbability=0.15, maxIter=20)
# results = graph.pageRank(resetProbability=0.15, tol=0.01)
# results.vertices.sort('pagerank',ascending=False).show()

# 标签传播算法
# graph.labelPropagation(maxIter=20).show()

# 宽度优先
# graph.bfs('id="e"', 'id="b"').show()

# 最短路径--Dijstra
# graph.shortestPaths(landmarks=['a']).show()

# 三角形计数
# graph.triangleCount().show()

# 连通分量
# spark.sparkContext.setCheckpointDir('checkpoint')
# graph.connectedComponents().show()
# graph.stronglyConnectedComponents(maxIter=10).sort('component', ascending=False).show()


# 绘制无向图
def PlotGraph(edge_list):
    Gplot=nx.Graph()
    for row in edge_list.select('src','dst').take(1000):
        Gplot.add_edge(row['src'],row['dst'])
    nx.draw(Gplot, with_labels=True, font_weight='bold')
    plt.show()

# 绘制有向图
def PlotDiGraph(edge_list):
    Gplot=nx.DiGraph()
    for row in edge_list.select('src','dst').take(1000):
        Gplot.add_edge(row['src'],row['dst'])
    nx.draw(Gplot, with_labels=True, font_weight='bold')
    plt.show()

PlotDiGraph(graph.edges)
