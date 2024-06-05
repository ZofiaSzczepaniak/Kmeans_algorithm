import matplotlib.pyplot as plt
import math as m
import json


def newcentroids(points):
    # This function takes points from the input data (the list of points).
    xsum = 0
    ysum = 0
    c = []
    for i in points:  # Loop is going through all points in cluster.
        xsum = xsum + i[0]
        ysum = ysum + i[1]
    if len(points) != 0:
        xavg = xsum / len(points)
        yavg = ysum / len(points)
    else:
        xavg = 0
        yavg = 0
    c = [xavg, yavg]
    return c  # This function returns list of one x and one y (one centroid - the middle of the cluster).


def clustering(points, centroids):
    # I create function which takes points from the input data and the list of centroids.
    clusters = [[] for i in range(k)]  # I create the list of clusters.
    for point in points:  # For every point in text:
        c = 0  # This variable will contain the information about the nearest centroid for the point.
        min = float('inf')  # I create the variable, which helps cluster the points.
        for z in centroids:  # Loop is going through all centroids.
            d = m.sqrt((point[0] - z[0]) ** 2 + (point[1] - z[1]) ** 2)
            if d < min:
                min = d
                c = z
        clusters[centroids.index(c)].append(point)  # The cluster index is defined by the centroids index.
    return clusters


# This function returns the list of clusters.
def silhouette(centroids, clusters):
    # I create the function, which takes the list of centroids and the list of clusters and returns the average silhouette coefficient.
    silhouettes = []  # This table will contain the silhouette coefficient for every point in the cluster.
    for idx, cluster in enumerate(clusters):  # This loop is going through all clusters and their indexes.
        # (Function enumerate creates the pair of indices and clusters).
        for point in cluster:  # The loop is going through all points in the cluster.
            a = 0  # This variable will contain the average distance from a point to all other points in the same cluster.
            for point2 in cluster:
                if point != point2:
                    a += m.sqrt((point[0] - point2[0]) ** 2 + (point[1] - point2[1]) ** 2)
            if len(cluster) > 1:  # I prevent division by zero.
                a = a / len(cluster)
            else:
                a = 0

            b = float('inf')
            for other_cluster_idx, other_cluster in enumerate(clusters):
                if idx != other_cluster_idx:
                    b_temp = 0  # This variable will contain the average distance from point i to all points in the nearest cluster.
                    for point2 in other_cluster:
                        b_temp += m.sqrt((point[0] - point2[0]) ** 2 + (point[1] - point2[1]) ** 2)
                    if len(other_cluster) == 0:  # I prevent division by zero.
                        b_temp = b_temp / 1
                    else:
                        b_temp = b_temp / len(other_cluster)
                    if b_temp < b:
                        b = b_temp

            if a > b:  # I prevent division by zero.
                s = (b - a) / a
            elif b > a:
                s = (b - a) / b
            elif a == 0 or b == 0:
                s = 0
            silhouettes.append(s)
        plt.plot(sorted(silhouettes, reverse=True))  # I generate silhouette plots.
    plt.title(f"The number of clusters {len(centroids)}")
    plt.grid()
    plt.xlabel("Points of clusters")
    plt.ylabel("Silhouette score")
    plt.savefig(f'Silhouette_for_{len(centroids)}.png')
    plt.show()
    silhouetteavg = sum(silhouettes) / len(silhouettes)  # I calculate the average silhouette coefficient.
    return silhouetteavg


text = []  # I create empty list text.
with open("data.json") as f:  # I open file as a string. Method open takes text and mode ("r" is read mode).
    text = json.load(f)
silhouettescores = []  # I create the table which will contain the silhouette scores.
for l in range(1, 6):  # The loop is going through all k.
    k = l + 1  # I define k.
    p1 = text[0]
    # The first centroid will be the first point of the data.
    centroids = []
    centroids.append(p1)
    sumd = 0  # I define the sum of all distances.
    for j in range(k - 1):  # The loop goes through all k (all centroids for some k).
        max = 0  # I create the variable, which is helpful to look for centroids (the most remote points from other centroids).
        for i in text:  # Loop is going through all points.
            sumd = 0
            for z in centroids:  # Loop is going through all centroids.
                sumd = sumd + m.sqrt((i[0] - z[0]) ** 2 + (i[1] - z[1]) ** 2)
                if max < sumd:
                    max = sumd
                    px = i
        centroids.append(px)
        p1 = px
    clusters = clustering(text, centroids)
    newcen = []
    for cluster in clusters:
        newcen.append(newcentroids(cluster))
    newclusters = clustering(text, newcen)
    for _ in range(10): #Iterations to improve clustering.
        newcen = []
        for cluster in newclusters:
            newcen.append(newcentroids(cluster))
        newclusters = clustering(text, newcen)
    silhouetteavg = silhouette(newcen, newclusters)  # I calculate the average silhouette coefficient and I add it to the coefficient scores.
    silhouettescores.append(silhouetteavg)
    for i in range(k):
        plt.plot([elem[0] for elem in newclusters[i]],[elem[1] for elem in newclusters[i]],'o')
        plt.scatter(newcen[i][0] , newcen[i][1] , s = 80, color = 'k')
        plt.title(f"The number of clusters ={l+1}")
    plt.savefig(f'clusters{k}.png')
    plt.show()
    # I show all the plots for each k.
for l in range(1, 6):
    print(
        f"Średni silhouette score dla k = {l + 1}: {silhouettescores[l - 1]}")  # and I print the silhouette scores for each k.
    # The best k: k=5.