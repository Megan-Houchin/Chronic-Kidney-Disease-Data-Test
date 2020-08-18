#Project 2 Step 4 driver
#*****************************************
# YOUR NAME: Megan Houchin
# NUMBER OF HOURS TO COMPLETE: 7 hours

#import statements
import KMeansClustering_functions as kmc #Use kmc to call your functions

#Main
glucose, hemoglobin, classification = kmc.openckdfile()
kmc.graphDataOriginal(glucose, hemoglobin, classification) #graph original true data

centroids = kmc.select(2) #enter number of clusters here

#new cases
new_centroids, new_classification = kmc.iterate(centroids, hemoglobin, glucose)
kmc.graphDataNew(glucose, hemoglobin, new_classification, new_centroids)
print("The centroid is: ")
print(new_centroids)
print()
kmc.compare(classification, new_classification)
