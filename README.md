## Day 01

Exploring the basics of Tensorflow and its API usage in python  
[`api.py`]()

# Exploring **SUPERVISED LEARNING**
 -  teaching a computer using examples.  
 - a computer is shown many labeled examples, and it learns to make predictions or decisions based on that data.  

<details> <summary> <b><b>Types</b></b> </summary>  

    1. Linear Regression  
    2. Logistic Regression  
    3. Decision Trees  
    4. Random Forests  
    5. Support Vector Machines(SVM's)  
</details>  

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
<details><summary> <b><b>Types</b></b> </summary> 

    1. K- means clustering  
    2.  hierarchical clusturing  
    3. Principal component Analysis  
</details>  

1. **K-means clustering**  

- (It is a way to group a bunch of data points into clusters based on their features.)  
- (The idea behind K-means is to split these dots into "K" number of groups.)  
 *STEPS* :- 
 1. `Choose K`: Decide how many clusters (K) you want.

2. `Place K centroids`: These are initial points (think of them as centers) placed randomly on the scatter plot.

3. `Assign points to clusters`: Each dot (data point) is assigned to the nearest centroid.

4. ` Recalculate centroids`: For each cluster, calculate the new centroid by finding the average of all the data points in the cluster.

5. `Repeat`: Reassign data points to the nearest centroid and recalculate the centroids.  

    [Kmeans.ipynb](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/Kmeans.ipynb)  

## Day 06  

2. **Hierarchical Clustering**  

- (It is a method that groups similar data points together based on their similarity or dissimilarity.)    
- (It results in hierarchical structure.)  
- (Can be visualized as a dendrogram(shows order in which cluster were merged).)  

<details>
<summary> Advantages </summary>  

 1. it doesn't require specifying the number of clusters in advance, allowing for an automatic determination based on the data. 
 2. it provides an intuitive visualization through dendrograms, enabling us to explore different clustering possibilities.  
 3. it captures hierarchical relationships which can reveal nested structures within the data.  
</details>

 <details><summary> Limitations </summary>  
 
1. expensive, particularly for large datasets due to the need to compute pairwise distances.  
2. It can also be sensitive to noise and outliers affecting the clustering results. 
3. dealing with categorical or mixed data types can be challenging in hierarchical clustering.  
</details>  

[hierarchical.ipynb](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/hierarchical.ipynb)  


3. **PCA (Principal Component Analysis)**  

- ( technique used to reduce the dimensionality of a dataset whilst retaining as much of the original information as possible.)  
- (This method is excellent for simplifying data while keeping its essential patterns, making it easier to analyze and visualize.)  

## Day 07

# Exploring **DL NEURAL NETWORKS**  

- Neural networks are inspired by the structure and function of the **human brain**, which consists of billions of neurons that communicate with each other through electrical signals.  
- designed to mimic this brain-like behavior to solve complex problems.  
- composed of layers of artificial neurons (units or nodes).  
        -  first layer is called the **`input layer`**, which receives the    data that we want to analyze or manipulate.  
        -  The last layer is called the **`output layer`**, which produces the result or prediction that we are interested in.  
        -  In between the input and output layers, there can be one or more **`hidden layers`** which perform intermediate computations and transformations on the data.  
<br>  

  ![Deep Neural Network](https://www.ibm.com/content/dam/connectedassets-adobe-cms/worldwide-content/cdp/cf/ul/g/3a/b8/ICLH_Diagram_Batch_01_03-DeepNeuralNetwork.png)  
<details><summary> <b>Types</b> </summary>
    
    1. Feedforward Neural Networks (FNN)  
    2. Convolutional Neural Networks (CNN)  
    3. Recurrent Neural Networks (RNN)  
</details>  

______________
**1. FNN** 

- processes data in `one direction`—from input to output—without looping back.
- connections between the nodes do not form cycles.
- The network consists of an input layer, one or more hidden layers, and an output layer. 
  
  [FNN.ipynb](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/FNN.ipynb)  
  [train.csv](https://github.com/sachinkhote/Python-and-Tensorflow-for-ML/blob/main/train.csv) (dataset)
<br><br>

  ![FNN](https://upload.wikimedia.org/wikipedia/commons/5/54/Feed_forward_neural_net.gif)  
<br>  
  
## Day 08
**2. CNN**  

- designed to effectively process grid-like data, such as images.  
- specifically designed to handle image data.  
- 1. `<Convolutional Layer>` - this layer scans the image with small filters, these filters detect features such as edges, textures, or colors by looking at small sections of the image at a time.  
    2. `<Pooling Layer>` - responsible for the reduction of the size(downsamples).It is responsible for the reduction of the size.  
    3. `<Fully Connected Layer>` -  This is where the network makes sense of all the extracted features and makes a prediction. 
    4. `<Output Layer>` - Finally, the output layer provides the final result.  
<br><br><br>    

  ![CNN](https://editor.analyticsvidhya.com/uploads/568241-4.png)