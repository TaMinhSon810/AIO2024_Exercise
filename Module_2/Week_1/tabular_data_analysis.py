import pandas as pd
import numpy as np

df = pd.read_csv('AIO2024_Exercise/Module_2/Week_1/advertising.csv')
data = df.to_numpy()

# Question 15
sales_column = data[:, 3]
max_sales = np.max(sales_column)
max_sales_index = np.argmax(sales_column)
print(max_sales)
print(max_sales_index)

# Question 16
tv_column = data[:, 0]
mean_tv = np.mean(tv_column)
print(mean_tv)

# Question 17
count_sales_greater_20 = np.sum(sales_column >= 20)
print(count_sales_greater_20)

# Question 18
radio_column = data[:, 1]
mean_radio_sales_greater_15 = np.mean(radio_column[sales_column >= 15])
print(mean_radio_sales_greater_15)

# Question 19
newspaper_column = data[:, 2]
sum_sales_newspaper = np.sum(sales_column[newspaper_column > np.mean(newspaper_column)])
print(sum_sales_newspaper) 

# Question 20
average_sales = np.mean(sales_column)
scores = np.where(sales_column > average_sales, 'Good', np.where(sales_column < average_sales, 'Bad', 'Average'))
print(scores[7:10])

# Question 21
average_sales = np.mean(sales_column)
closest_to_average_sales = sales_column[np.abs(sales_column - average_sales).argmin()]
scores_1 = np.where(sales_column > closest_to_average_sales, 'Good', np.where(sales_column < closest_to_average_sales, 'Bad', 'Average'))
print(scores_1[7:10])
