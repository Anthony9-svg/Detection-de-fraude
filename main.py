from init import *
from algorithms import *
import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network
#affichage(noeuds,relations,all_cliques)

st.title("Detection de fraude")
st.write("La probabilité p est en fonction du nombre de noeuds n : log(n)+1/n")
n = st.text_input("Entrez le nombre de noeuds")

if st.button("Générer le graphe"):

    noeuds,relations = creer_graphe(n)
    graph=dictionnarize(noeuds,relations)
    max_clique = clique_maximum(graph)
    print(max_clique)

    net = Network(height="400px", width="100%", bgcolor="#ffffff", font_color="black")

    for node in noeuds:
        net.add_node(node,label=str(node))
    for i,j in relations:
        net.add_edge(i,j)
    net.force_atlas_2based()
    for node in net.nodes:
        if node["id"] in max_clique:
            node["color"]="red"
    net.save_graph("graph.html")
    HtmlFile = open("graph.html", "r", encoding="utf-8")
    source_code = HtmlFile.read()

    components.html(source_code, height=450, scrolling=True)
    