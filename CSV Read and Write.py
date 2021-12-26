import pandas as pd
lines=pd.read_csv('heart.csv') # Reading the CSV file
print(lines) # Printing the lines of the original CSV files
# Creating a DataFrame object and storing the information of two new patients
df=pd.DataFrame({'Patient 1':{'Age':50,'Sex':'M','ChestPainType':'ATA','RestingBP':150,'Cholesterol':200,'RestingECG':'ST','ST_Slope':'Flat','HeartDisease':1},
                'Patient 2':{'Age':7,'Sex':'F','ChestPainType':'AST','RestingBP':120,'Cholesterol':100,'RestingECG':'ST','ST_Slope':'Up','HeartDisease':0}}).T
df.to_csv('heart1.csv') # Writing the new data on a new file
newlines=pd.read_csv('heart1.csv')
print(newlines) # Printing the lines of the new CSV file