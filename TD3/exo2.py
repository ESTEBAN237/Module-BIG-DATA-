import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import exo1

def visualize_clusters(X, y):

    colors = list(mcolors.CSS4_COLORS.values())

    for cluster in set(y): #recuperer les valeurs unique de y represente les labels
        # Récupérer les points appartenant au cluster
        points = X[y == cluster]

        # Afficher les points avec une couleur différente
        plt.scatter(points[:, 0], points[:, 1],
                    color=colors[cluster])

    plt.show()

visualize_clusters(X,y)  