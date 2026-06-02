def coloration(G, sommets):
    couleurs = {}
    ordre = sorted(sommets, key=lambda v: len(G[v]), reverse=True)

    for v in ordre:
        interdites = {couleurs[u] for u in G[v] if u in couleur}        

        c = 1
        while c in interdites:
            c += 1

        couleurs[v] = c

    return couleurs


def expand(G, clique, candidats, meilleure):
    if len(clique) > len(meilleure):
        meilleure = clique.copy()

    if not candidats:
        return meilleure

    couleurs = coloration(G, candidats)

    ordre = sorted(
        candidats,
        key=lambda v: couleurs[v]
    )

    while ordre:
        v = ordre.pop()

        if len(clique) + couleurs[v] <= len(meilleure):
            return meilleure

        nouveaux_candidats = candidats & G[v]

        meilleure = expand(
            G,
            clique | {v},
            nouveaux_candidats,
            meilleure
        )

        candidats.remove(v)

    return meilleure


def clique_maximum(G):
    return expand(
        G,
        set(),
        set(G.keys()),
        set()
    )