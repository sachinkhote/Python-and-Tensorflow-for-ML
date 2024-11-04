## Day 01

Exploring the basics of Tensorflow and its API usage in python  
[`api.py`]()

# Exploring **SUPERVISED LEARNING**
 -  teaching a computer using examples.  
 - a computer is shown many labeled examples, and it learns to make predictions or decisions based on that data.  

types are:
- Linear Regression ,
- Logistic Regression,
- Decision Trees ,
- Random Forests ,
- Support Vector Machines(SVM's)

1. **Linear Regression** 

- (algorithm used to model the relationship between dependent variable and one or more independent variable. )  
- (goal is to find thye best fit line that describes the relationship between variables.)
() 


[linearRegression.ipynb](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/linearRegression.ipynb)   
[car_purchasing_data.csv](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/car_purchasing_data.csv) (dataset)

## Day 02

2. **Logistic Regression**

- (used to analyse the datasets with one or more independent variables)  
- (useful to predict the probability of an event occuring)  
- (in logistic Reg. dependent variable is binary that menas it has only two outcomes i.e., 1 or 0, Yes or No , true or False)    

   [logisticRegression.ipynb](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/logisticRegression.ipynb)  
[heartdiseases.csv](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/heartdiseases.csv) (dataset)

3. **Decision Tree**

- (used for both classification and regression tasks)  
- (it creates tree like structure which helps us to find out the insights)  
- (it generally uses divide_and_conquer strategy.)  

    [decisionTree.ipynb](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/decisionTree.ipynb)  
    [iris_tree.pdf](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/iris_tree.pdf)  

## Day 03  

4. **Random Forest**  

- (This is also used for both classification and regression tasks.)  
- (it is known for their ability to handle large datasets while providing accurate predictions.)  
- (it is a method which combines multiple decision tree to make prediction.)  
- (each single decision tree is built using random subset of trainig data.)  

    [RandomForest.ipynb](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/RandomForest.ipynb)  

## Day 04  

5. **Support Vector Machine (SVM)**  

- (it classifies the data by finding slickest decision boundry betw different classes.)  
- (Finding the hyperplane which seperates the classes within data sets with max. margin .)  
- (hyperplane is determined by the SVM , which are the data points closest to the decision boundry. )  
- (SVM's are generally adaptible coz they can handle both binary classification(yes/no) and regression(numerical values).)

[svm.ipynb](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/svm.ipynb)  

## Day 05

# Exploring **UNSUPERVISED LEARNING**  
- letting a computer figure things out on its own without any labeled examples.  
- the computer looks at data and tries to find patterns or groupings on its own.  

types / Algorithms are: 
 - K- means clustering  
 - hierarchical clusturing  
 - Principal component Analysis  

1. **K-means clustering**  

- (It is a way to group a bunch of data points into clusters based on their features.)  
- (The idea behind K-means is to split these dots into "K" number of groups.)  
 *STEPS* :- 
 1. `Choose K`: Decide how many clusters (K) you want.

2. `Place K centroids`: These are initial points (think of them as centers) placed randomly on the scatter plot.

3. `Assign points to clusters`: Each dot (data point) is assigned to the nearest centroid.

4. ` Recalculate centroids`: For each cluster, calculate the new centroid by finding the average of all the data points in the cluster.

5. `Repeat`: Reassign data points to the nearest centroid and recalculate the centroids.  

## Day 06  

2. **Hierarchical Clustering**  

- (It is a method that groups similar data points together based on their similarity or dissimilarity.)    
- (It results in hierarchical structure.)  
- (Can be visualized as a dendrogram(shows order in which cluster were merged).)  

*Advantages*  
 1. it doesn't require specifying the number of clusters in advance, allowing for an automatic determination based on the data. 
 2. it provides an intuitive visualization through dendrograms, enabling us to explore different clustering possibilities.
 3. it captures hierarchical relationships which can reveal nested structures within the data.  

 *Limitations*  
 1. expensive, particularly for large datasets due to the need to compute pairwise distances.  
 2. It can also be sensitive to noise and outliers affecting the clustering results. 
 3. dealing with categorical or mixed data types can be challenging in hierarchical clustering.