import TD-Exo1.py   

class TriFusion:
    def __init__(self):
        self.data = [4, 7, 1, 3, 8, 2]

    def Tri_liste(self, liste):
        return tri_bulle(liste)

    def mergeListe(self, L1, L2):
        """Fusionne deux sous-listes déjà triées en une seule liste triée."""
        resultat = []
        i = 0 
        j = 0 

        # Tant qu'il reste des éléments à comparer dans les deux listes
        while i < len(L1) and j < len(L2):
            if L1[i] <= L2[j]:
                resultat.append(L1[i])
                i += 1
            else:
                resultat.append(L2[j])
                j += 1

        # Si L1 a encore des éléments restants, on les ajoute
        while i < len(L1):
            resultat.append(L1[i])
            i += 1

        # Si L2 a encore des éléments restants, on les ajoute
        while j < len(L2):
            resultat.append(L2[j])
            j += 1

        return resultat


