import matplotlib.pyplot as plt
import numpy as np
#graph 1
x1 = [2000,2005,2010,2015,2020]
y1= [15,18,19,22,35]
plt.plot(x1,y1,marker='o',color = 'violet')
plt.xlabel("Year")
plt.ylabel("number of users (in Thousands)")
plt.show()
#graph 2
arr1 = [48,60,2]
labels1 = ['males','females','others']  
colors = ['yellow','hotpink','grey']
plt.pie(arr1,labels = labels1,colors=colors)
plt.legend(title = 'Genderwise Proportion of number of customers as of the year 2021 :')
plt.show()
#graph 3
x2 = ['Grocery','Wardrobe','Electronics','Books','Furniture']
y2 = [24,57,107,68,20]
plt.bar(x2,y2, color="lightgreen")
plt.xlabel("Category of items")
plt.ylabel("Profit made by the website in the year 2020")
plt.show()
#graph 4
x3 = ['Peter England','Canon Inc.','Sony Inc.','Xiomi','Apple Inc.','Samsung']
y3 = [2.7,4.6,3.5,4.5,4.8,2.2]
plt.barh(x3,y3,color="pink")
plt.ylabel("Popular Seller(Brand) Names")
plt.xlabel("Mean Customer Rating out of 5.0")
plt.show()
#graph 5
x4 = ['Grocery','Wardrobe','Electronics','Books','Furniture']
y4 = [5056,3269,25699,1509,31220]
plt.bar(x4,y4,color = 'orange')
plt.xlabel('Category of Item : ')
plt.ylabel('Average Product Retail Price in Rupees : ')
plt.show()
#graph 6
arr2 = [18,20,25,23,54,16,12,19,13,23,25,24,26,26,24,23,21,33,32,33,35,41,48,48,41,49,45,48,47,27,55,56,45,44,41,43,42,41,42,42,41,22,21,21,21,21,23,23,22,22,21,21,]
bins = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,70]
plt.hist(arr2,bins=bins,color = 'skyblue')
plt.xlabel('age groups')
plt.ylabel('number of customers (in thousands)')
plt.show()
#graph 7 : customer proportion(location wise)
x5 = ['Delhi','Mumbai','California','Canada','Washington D.C.','U.A.E','Bejing','Tokyo','others']
y5 = [10,12,15,8,12,9,17,14,18]
explode = [0.1,0.05,0.20,0.15,0.09,0.1,0.2,0.1,0.05]
plt.pie(y5,labels=x5,explode=explode,shadow = True,colors = ['pink','lightblue','lightgreen','hotpink','crimson','purple','violet','skyblue','grey'],autopct='%1.1f%%')
plt.legend(title = 'Proportion of customers location wise',bbox_to_anchor=(1,1))
plt.show()
#graph 8 profit of company v/s year
x6 = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,] 
y6=[0.1,0.8,1,1.5,-2.4,3.1,07.5,4.7,14,5.0,1.0,12,-0.5,1.0,2.7,5.0,15.0,30.5,28,20,31,35,12]
plt.plot(x6,y6,marker = 'o',color = 'green')
plt.xlabel("Financial Year :")
plt.ylabel("Profit made by our website : ")
plt.show()
#graph 9 number of  complains v/s year
x7 = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,] 
y7=[1,8,1,15,4,31,75,47,150,10,12,5,10,27,50,150,35,28,20,31,35,12,13]
plt.plot(x7,y7,marker = 'o',color = 'red')
plt.xlabel("Financial Year :")
plt.ylabel("No. of complains recived that year : ")
plt.show()
#graph 9 number of sellers and location
country = ['China','Japan','USA','Korea','India','Others']
seller = [15,7,4,5.8,3,5]
colors = ["red",'hotpink','Blue','violet','lightblue','lightgreen']
plt.barh(country,seller,color=colors)
plt.ylabel("country")
plt.xlabel("number of sellers in thousands")
plt.show()