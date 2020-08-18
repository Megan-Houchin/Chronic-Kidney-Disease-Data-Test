#Project 2 Step 4 functions
#*****************************************
# YOUR NAME: Megan Houchin
# NUMBER OF HOURS TO COMPLETE: 7 hours
#import statements
import numpy as np
import matplotlib.pyplot as plt

#Functions
def openckdfile():
    #takes no arguments
    #this function opens the cvs file ckd and creates three arrays (one for each column of data) and then normalizes the data so that their range is from 0-1 inclusive and can be compared directly
    #returns the three arrays glucose, hemoglobin, and classification
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    glucose_scaled = ((glucose-70)/(490-70))
    hemoglobin_scaled = ((hemoglobin-3.1)/(17.8-3.1))
    return glucose_scaled, hemoglobin_scaled, classification

def select(K):
    #takes the argument K, an int of how many centroids should be created
    #creates a 2D array of randomly determined centroid points
    #returns the 2D centroid array
    return np.random.random((K, 2))

def assign(centroids, hemoglobin, glucose):
    #takes the three arrays centroids, hemoglobin, and glucose
    #assigns the values in hemoglobin and glucose the number specifying the cluster it is closest to
    #returns the array of cluster assignments
    K = centroids.shape[0]
    distances = np.zeros((K, len(hemoglobin))) #2D array of the distances each point is from each centroid
    for i in range(K):
        #g and h are y and x values of a centroid
        g = centroids[i,1] #i = the number of the specified centroid
        h = centroids[i,0]
        distances[i] = np.sqrt((hemoglobin-h)**2+(glucose-g)**2)
    assignments = np.argmin(distances, axis = 0) #the assignment of each coordinate
    return assignments

def update(centroids, hemoglobin, glucose, assignments):
    #takes the four arrays centroids, hemoglobin, glucose, and assignments
    #averages the x and y values of the points assigned to each centroid and averages them and updates the centroids
    #returns the updated centroid array
    K = centroids.shape[0] #number of centroids
    sumx = 0
    sumy = 0
    count = 0
    for i in range(K): #number of cluster
        for j in range(len(assignments)): #runs through all cluster assignments
            if i == assignments[j]:
                sumx += hemoglobin[j]
                sumy += glucose[j]
                count += 1
        if(count != 0): #checks for the case that no values are assigned this centroid
             centroids[i, 0] = sumx/count
             centroids[i, 1] = sumy/count
             sumx = 0  #resets values
             sumy = 0 
             count = 0
    return centroids
        
    
def iterate(centroids, hemoglobin, glucose):
    #takes centroid, glucose, and hemoglobin arrays
    #runs update and assign until centroid values no longer change
    #returns final centroid values and final classification of cluster values array
    test = True
    oldcent = np.copy(centroids)
    while(test):
        assignments = assign(centroids, hemoglobin, glucose)
        centroids = update(centroids, hemoglobin, glucose, assignments)
        if(np.array_equal(oldcent, centroids)):
            test = False
        else:
            oldcent = np.copy(centroids)
    new_classification = assignments
    return centroids, new_classification
        
def graphDataOriginal(glucose, hemoglobin, classification):
    #takes the three arrays glucose, hemoglobin, and classification
    #plots the data points in a hemoglobin vs glucose plot and color codes the classifications/clusters of each point
    #returns none
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "CKD")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "not CKD")
    plt.title('Data for Chronic Kidney Disorder')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    return None

def graphDataNew(glucose, hemoglobin, classification, centroids):
    #takes the four arrays glucose, hemoglobin, classification, and centroids
    #plots the data points in a hemoglobin vs glucose plot and color codes the classifications/clusters of each point, cannot plot more than 4 clusters
    #returns none
    K = centroids.shape[0] #number of centroids
    plt.figure()
    if(K == 2):
        plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "not CKD")
        plt.plot(centroids[0,0],centroids[0,1], "c.", markersize = 18, marker = '*')
        plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "CKD")
        plt.plot(centroids[1,0],centroids[1,1], "y.", markersize = 18, marker = '*')
    else: 
        plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
        plt.plot(centroids[0,0],centroids[0,1], "c.", markersize = 18, marker = '*')
        if(K > 1):
            plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
            plt.plot(centroids[1,0],centroids[1,1], "y.", markersize = 18, marker = '*')
        if(K > 2):
            plt.plot(hemoglobin[classification==2],glucose[classification==2], "b.", label = "Class 2")
            plt.plot(centroids[2,0],centroids[2,1], "tab:purple", markersize = 18, marker = '*')
        if(K > 3):
            plt.plot(hemoglobin[classification==3],glucose[classification==3], "m.", label = "Class 3")
            plt.plot(centroids[3,0],centroids[3,1], "g.", markersize = 18, marker = '*')
    plt.title('K-Means Clustering Results')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    return None

def t_positive(classification, new_class):
    #takes the arrays classification and new_class as arguments
    #determines True Positive Rates: number of correct CKD positive diagnoses
    #returns the percentage of True Positive
    correct = 0
    count = 0
    for i in range(len(new_class)):
        if(classification[i] == 0): #ones that are actually positive
            if classification[i] == new_class[i]: #and test CKD positive
                correct += 1
            count += 1
    return round((correct/count)*100, 2)

def f_positive(classification, new_class):
    #takes the arrays classification and new_class as arguments
    #determines False Positive Rates: number of incorrect CKD positive diagnoses
    #returns the percentage of False Positive
    count = 0
    incorrect = 0
    for i in range(len(new_class)):
        if(classification[i] == 1): #where they are not CKD
            if classification[i] != new_class[i]: #but test positive
                incorrect += 1
            count+=1
    return round((incorrect/count)*100, 2)

def t_negative(classification, new_class):
    #takes the arrays classification and new_class as arguments
    #determines True Negative Rates: number of non-CKD patients correctly labeled as non-CKD
    #returns the percentage of True Negative
    correct = 0
    count = 0
    for i in range(len(new_class)):
        if(classification[i] == 1): #where they are not CKD
            if classification[i] == new_class[i]: #and also test negative
                correct += 1
            count+=1
    return round((correct/count)*100, 2)

def f_negative(classification, new_class):
    #takes the arrays classification and new_class as arguments
    #determines False Negative Rates: number of non-CKD patients incorrectly labled
    #returns the percentage of False Negative
    count = 0
    incorrect = 0
    for i in range(len(new_class)):
        if(classification[i] == 0): #they are CKD positive
            if classification[i] != new_class[i]: #but test negative
                incorrect += 1
            count+=1
    return round((incorrect/count)*100, 2)

def compare(classification, new_class):
    #takes the arrays classification and new_class as arguments
    #starts by making sure the data can be compared to the original correctly. by this is mean even though it did cluster the data into groups, it had no way of knowing which should be 1 and which should be 0
    #so, it could have clustered the groups accurately, but the ones and zeros may need to be flipped. After this, it determines the number of true positives, false positives, true negatives, and false positives;
    #and prints the results
    #returns none
    zeros = 0
    ones = 0
    for i in new_class:
         if i == 0:
             zeros += 1
         else:
            ones+= 1
    if(zeros < ones): #if it flipped the trend, it did distinguish between the groups just not in the order desired, 
        #aka was still successful, but to compare must re-assign values
        for i in range(len(new_class)):
            if new_class[i] == 0:
                new_class[i] = 1
            else:
                new_class[i] = 0
    print("True Positives: " + str(t_positive(classification, new_class)) + "%")
    print("False Positives: " + str(f_positive(classification, new_class)) + "%")
    print("True Negatives: " + str(t_negative(classification, new_class)) + "%")
    print("False Negatives: " + str(f_negative(classification, new_class)) + "%")
    return None
            
            