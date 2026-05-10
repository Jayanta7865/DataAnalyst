#Pandas is powerfull data manipulation library in python,
# widely use for data anlysis and data cleaning.It provide two primary
#data structures:i)Series, ii)Dataframe. Series is one dimensional
#and Dataframe is a two dimensional.
# It helps you work with tables,clean data,analyze datasets,and handle CSV/Excel files easily.
import pandas as pd
##Create Series
data=[1,2,3,4,5] ##Example of serirs
df=pd.Series(data)
print(df)
##Print custom index
i=['A','B','C','D','E']
df=pd.Series(data,index=i)
print(df)
##Create Dataframe
new_data={
    "Name":["Jayanta","Sunama",'Mahadeb','Narayan','Debotosh'],
    "Age":[22,21,22,23,23],
    "City":['Kolkata','Bengaluru','Goa','Delhi','UP']
}
df=pd.DataFrame(new_data)  ##Example of Dataframe
print(df)
print(df.to_string(index=False)) ##can not print index number

 #Read CSV File
df=pd.read_csv("data.csv")
print(df)

### Basic Function

#head()

