#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:wangshuai

from pygraph.classes.digraph import digraph
class PRIterator:
    __doc__ = '''计算一张图中的PR值'''

    def __init__(self, dg):
        self.damping_factor = 0.85 # 阻尼系数,即α
        self.max_iterations = 100 # 最大迭代次数
        self.min_delta = 0.00001 # 确定迭代是否结束的参数,即ϵ
        self.graph = dg


    def page_rank(self):
        #  先将图中没有出链的节点改为对所有节点都有出链
        for node in self.graph.nodes():
            if len(self.graph.neighbors(node)) == 0:
                for node2 in self.graph.nodes():
                    digraph.add_edge(self.graph, (node, node2))

        #获取图中的顶点以及顶点总数
        nodes = self.graph.nodes()
        graph_size = len(nodes)

        #若图为空，直接返回，程序结束
        if graph_size == 0:
            return {}

        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # 给每个节点赋予初始的PR值
        damping_value = (1.0 - self.damping_factor) / graph_size # 公式中的(1−α)/N部分

        flag = False # flag:迭代结束的标志，初始为false；当为true迭代结束

        for i in range(self.max_iterations):
            change = 0 # 记录与上一次迭代结果的差距
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):  # 遍历所有“入射”的页面
                    rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
                rank += damping_value
                change += abs(page_rank[node] - rank)  # 绝对值
                page_rank[node] = rank


            print("This is NO.%s iteration" % (i + 1))
            print(page_rank)

        while change < self.min_delta:
            flag = True
            break
        if flag: #通过flag判断迭代是否结束，并输出最后迭代计算的节点
            print("finished in %s iterations!" % node)
        else:
            print("finished out of 100 iterations!")
        return page_rank # 最后还需要将计算得到的字典page_rank返回

    def read_data(path):
        node_list = []
        edge_list = []
        with open(path) as f:
            lines = f.readlines()
            nodes = lines[1].split(" ")
            nodes[-1] = nodes[-1].split("\n")[0]
            for node in nodes:
                node_list.append(node)
            edges = lines[3:]
            for edge in edges:
                edge = edge.split(" ")
                edge[1] = edge[1].split("\n")[0]
                edge_list.append(edge)
            return node_list,edge_list

if __name__ == '__main__':
    dg = digraph()
    path = './pagerank_four_nodes.txt'
    # path = './/实验七测试文件/pagerank_seven_nodes.txt'
    node_list, edge_list = PRIterator.read_data(path)
    print('顶点信息：', node_list)
    print('边信息：', edge_list)
    dg.add_nodes(node_list)
    for edg in edge_list:
        dg.add_edge(edg)
    pr = PRIterator(dg)
    page_ranks = pr.page_rank()
    print("The final page rank is\n", page_ranks)


