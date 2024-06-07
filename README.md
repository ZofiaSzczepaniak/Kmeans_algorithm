# Kmeans_algorithm
Implementation of k-means algorithm. The program finds the optimal number of clusters, using silhouette analysis. It also generates silhouette plots and provides silhouette scores.
K-means clustering is an unsupervised machine learning algorithm that partitions a dataset into k distinct clusters, where each data point belongs to the cluster with the nearest mean, serving as the cluster center. The algorithm iteratively updates cluster centers and reassigns data points to minimize the within-cluster sum of squares, aiming for compact and well-separated clusters.
The project contains three files:
1) k-means - the implementation of k-means algorithm.
2) data.json - the file json with data, which is used for clustering in the main program.
# Results
The optimal number of clusters is five. The visualization of clusters:

![image](https://github.com/ZofiaSzczepaniak/Kmeans_algorithm/assets/169342885/5a7df037-2ee6-4c73-b116-e023a141c358)

The silhouette score for five clusters:

![image](https://github.com/ZofiaSzczepaniak/Kmeans_algorithm/assets/169342885/452613ea-7b0f-49fe-86ce-aece28a9f71e)

# Instructions: 
First to use the program, one must install the Python compiler. To do so, enter the site and follow the given steps: https://code.visualstudio.com/
