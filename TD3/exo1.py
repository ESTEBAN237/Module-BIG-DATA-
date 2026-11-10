from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=500, centers=5, n_features=2,
                  random_state=0)

print(X.shape)
print (y)

plt.scatter(X[:, 0], X[:, 1], c=y)  

# Notes 
# X[:,0]  On Prend toutes les lignes et seulement la premiere colonne 
# c(couleur)=y veut dire puisque y  represente les labels de chaque points alors on vas les utiliser
# pour définir la couleur de chauqe points du clusters 

plt.xlabel("Caractéristique 1")
plt.ylabel("Caractéristique 2")
plt.title("Génération de 5 clusters")

plt.show()