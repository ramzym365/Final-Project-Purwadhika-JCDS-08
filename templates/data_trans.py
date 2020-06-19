import pandas as pd 

# to read csv file named "samplee" 
df = pd.read_csv(r"E:\Job Connector Data Science Purwadhika\Module-03-Machine Learning\ulikan\Untitled Folder\templates\xxx.csv") 
df.drop('Unnamed: 0', axis = 1, inplace = True)
df = df.head()

# to save as html file 
# named as "Table" 
df.to_html("dataset.html") 

