#Project 2 Steps 2 and 3
#*****************************************
# YOUR NAME: Megan Houchin
# NUMBER OF HOURS TO COMPLETE: 3 hours

#import statements
import numpy as np
import matplotlib.pyplot as plt
import random
import math


# FUNCTIONS
def openckdfile():
    #takes no arguments
    #this function opens the cvs file ckd and creates three arrays (one for each column of data)
    #returns the three arrays glucose, hemoglobin, and classification
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


def normalizeData(glucose, hemoglobin, classification):
    #takes the three arrays as arguments
    #normalizes the data and saves these new values in new arrays (makes data unitless and between values of 0 and 1 inclusive)
    #returns the normalized arrays
    glucose_scaled = ((glucose-70)/(490-70))
    hemoglobin_scaled = ((hemoglobin-3.1)/(17.8-3.1))
    return glucose_scaled, hemoglobin_scaled, classification

def graphData(glucose, hemoglobin, classification):
    #takes three arrays as arguments
    #displays each arrays' data in a plot and distinguishes the data by color coding them (class 1 is black and class 0 is red)
    #returns no value
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "CKD")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "not CKD")
    plt.title('Data for Chronic Kidney Disorder')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    return None

def createTestCase():
    #takes no arguments
    #creates a random hemoglobin float between 0 and 1 and a random glucose float between 0 and 1
    #returns the new floats
    newhemoglobin = round(random.uniform(0,1), 8)
    newglucose = round(random.uniform(0,1), 8)
    return newhemoglobin, newglucose

def calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled):
    #takes the random glucose and hemoglobin values (floats) and the normalized glucose and hemoglobin arrays
    #creates a list of distances between the random hemoglobin, glucose point and every point on the plot and puts these distances into an array
    #returns the array of distances
    distances = []
    length = glucose_scaled.size
    for i in range(length):
        distances.append(math.sqrt((glucose_scaled[i]-newglucose)**2+(hemoglobin_scaled[i]-newhemoglobin)**2))
    dist_array = np.array(distances)
    return dist_array

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification):
    #takes the random glucose and hemoglobin values (floats) and the normalized glucose and hemoglobin arrays as well as the classification array
    #determines the class of the nearest value to the random glucose and hemoglobin values 
    #returns the class of the point nearest to the random glucose and hemoglobin values 
    distAr = calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
    min_index = np.argmin(distAr)
    nearest_class = classification[min_index]
    return nearest_class

def graphTestCase(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification, k):
    #takes the random glucose and hemoglobin values (floats) and the normalized glucose and hemoglobin arrays as well as the classification array. It also takes k, the number of cases nearest to the unknown point
    #plots the original plot of all the data points as well as the new one, but the new one is bigger than the rest
    #returns none
    gluc_arr = np.array(newglucose)
    hemo_arr = np.array(newhemoglobin)
    class_arr = np.array(kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification))
    plt.figure()
    plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "CKD")
    plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "not CKD")
    
    plt.plot(hemo_arr[class_arr==1],gluc_arr[class_arr==1], "k.", markersize = 20)
    plt.plot(hemo_arr[class_arr==0],gluc_arr[class_arr==0], "r.", markersize = 20)
    plt.title('Test Case for Chronic Kidney Disorder')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    return None

def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification):
    #takes the arguments k, the number of points tested closest to the point in question, the random glucose and hemoglobin values (floats) and the normalized glucose and hemoglobin arrays as well as the classification array
    #determines the classes of k number of points closest to the unknown point and determines which classification mostly surrounds the unknown point
    #returns the class the unknown point most likely is based on its surrounding points
    distAr = calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
    sorted_indices = np.argsort(distAr)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    ones = 0
    zeros = 0
    for i in k_classifications:
        if(i == 1):
            ones += 1
        else:
            zeros += 1
    if(ones >= zeros):
        new_class = 1.0
    else:
        new_class = 0.0
    return new_class

# MAIN SCRIPT
#base data
glucose, hemoglobin, classification = openckdfile() 
glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose, hemoglobin, classification)
graphData(glucose_scaled, hemoglobin_scaled, classification)
#new case
newhemoglobin, newglucose = createTestCase()
graphTestCase(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification, 5)

answer1 = "not CKD"
answer2 = "not CKD"
if(nearestNeighborClassifier(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification) == 1):
    answer1 = "CKD"
if(kNearestNeighborClassifier(5, newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification) == 1):
    answer2 = "CKD"

print("Its nearest neighbor is " + answer1)
print("The majority of its 5 nearest neighbors are " + answer2)

