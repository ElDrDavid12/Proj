import statistics
import csv

#leer los ladots de ventas mensuales desde un archivo CSV
monthly_sales = {}
with open('python/monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

#hallar media
mean_sales = statistics.mean(sales)
print("La media es: ", mean_sales)

#hallar mediana
median_sales = statistics.median(sales)
print("La mediana es: ", median_sales)

#hallar moda
mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales}")

#Desviacion Estandar
stdev_sales = statistics.stdev(sales)
print(f"La desviacion estandar es: {stdev_sales}")

#Hallar la varianza
variance_sales = statistics.variance(sales)
print(f"La varianza es: {variance_sales}")

#hallar el range
range_sales = max_sales - min_sales
print(f"El rango de ventas: {range_sales}")
