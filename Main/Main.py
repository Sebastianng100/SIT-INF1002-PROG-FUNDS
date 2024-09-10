#Main.py will be where we do the master codes and the shared codes
#Please do read the README.md file to understand the project and steps to take

#Introducing libraries
import pandas as pd

#Reading of dataset files
enron_dataset = pd.read_csv(r'data/enronData.csv')
print("Hello this is the dataframe:" + str(enron_dataset))