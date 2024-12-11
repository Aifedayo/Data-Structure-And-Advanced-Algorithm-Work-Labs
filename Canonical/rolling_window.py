def moving_average_sales(sales_data, window=3):
    sales = [item[1] for item in sales_data]
    return sum(sales[-window:])/window


sales_data = [(1, 160), (2, 170), (3, 180), (4, 170), (5, 160)]
print(moving_average_sales(sales_data))