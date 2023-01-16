import pandas as pd
import matplotlib.pyplot as po


data = pd.read_csv('C:\\Users\\ASUS\\Desktop\\Code\\sales_data.csv')

df = pd.DataFrame(data)
X = list(df.iloc[:, 1])
Y = list(df.iloc[:, 2])
po.bar(X, Y, color='g')
po.title("Data show")
po.xlabel("Sales")
po.ylabel("Category")
  
# Show the plot
po.show()
