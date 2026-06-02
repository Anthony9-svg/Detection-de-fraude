from random import random,shuffle
from math import log 
from collections import Counter
#import streamlit as st

def creer_graphe(n):
    n=int(n)
    p = (log(n)+1)/n

    noeuds = [i for i in range(n)]
    relations = set()

    for i in noeuds:
        for j in noeuds:
            if random() <= p and i<j:
                relations.add((i,j))
            
    return noeuds,relations

def dictionnarize(noeuds,relations):
    graph = {noeud: set() for noeud in noeuds}
    for i, j in relations:         
        graph[i].add(j)
        graph[j].add(i)
    return graph   
#labels = {node: node for node in graph}
"""
def most_frequent_neighbor_label(node, graph, labels):
    neighbor_labels = [labels[n] for n in graph[node]]
    if not neighbor_labels:
        return labels[node]
    return Counter(neighbor_labels).most_common(1)[0][0]
 
def label_propagation(graph, max_iter=100):
    labels = {node: node for node in graph}
 
    for _ in range(max_iter):
        nodes = list(graph.keys())
        shuffle(nodes)         
 
        changed = False
        for node in nodes:
            new_label = most_frequent_neighbor_label(node, graph, labels)
            if new_label != labels[node]:
                labels[node] = new_label
                changed = True
 
        if not changed:               
            break
 
    return labels
 

def get_communities(labels):
    communities = {}
    for node, label in labels.items():
        communities.setdefault(label, []).append(node)
    return list(communities.values())
 """


