This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

This code was created by Megan Houchin :)

NearestNeighborClassification:
This program uses K-Nearest Neighbor Classification to determine if a new randomized data point would be more likely to test positive or negative for Chronic Kidney Disease (CKD). This program first normalizes the known data, given by the ckd.csv file, so they can be unit-less values and can be directly graphed against one another since they share the same 0-1 scale. It then plots the known data points on a hemoglobin vs. glucose plot, each axis ranging from 0-1. A random test case is the created and is determined to be CKD positive or negative based on the closest value to it on the plot. Using K-Nearest Neighbor Classification, this prediction becomes more accurate since one can use more than one case as long as the cases tested are an odd number (avoiding ties). This number can be adjusted when calling graphTestCase in main (the current number is 5).

K-Means Clustering:
This program uses K-Means Clustering to find groups within a set of data. It does this by creating a random point (or more) and assigning the points nearest to each. Then it updates these points by taking the mean of all the points assigned to each random point respectively. The intent is to find the center of each "cluster" and the random point will eventually become the "centroid". After iterating between assignments and updates, the eventually all the points will be assigned the proper centroid and the centroids will no longer update since they are in the middle of each cluster. The plot is then printed with the centroids of each cluster indicated with a star of different colors and each cluster has their own color. Up to 4 clusters may be plotted, but more than 4 clusters may be created. In order to change the number of clusters in KMeansCluster_driver, you can change the number sent in centroids = kmc.select(2) which is currently 2. When creating clusters of 2, the results are calculated using the compare function, as it compare the clusters' data to the correct data in the csv file and prints their accuracy results. 

pseudocode:
def openfileckd():
- No arguments
- Creates 3 arrays and normalizes data
- Returns the normalized arrays
def select(K):
- takes the argument K, an int of how many centroids should be created
- creates a 2D array of randomly determined centroid points
- returns the 2D centroid array
def assign(centroids, hemoglobin, glucose):
- takes the three arrays centroids, hemoglobin, and glucose
- assigns the values in hemoglobin and glucose the number specifying the cluster it is closest to
- returns the array of cluster assignments
def update(centroids, hemoglobin, glucose, assignments):
- takes the four arrays centroids, hemoglobin, glucose, and assignments
- averages the x and y values of the points assigned to each centroid and averages them and updates the centroids
- returns the updated centroid array
def iterate(centroids, hemoglobin, glucose):
- takes centroid, glucose, and hemoglobin arrays
- runs update and assign until centroid values no longer change
- returns final centroid values and final classification of cluster values array


