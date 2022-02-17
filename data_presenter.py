# Create a new file called data_presenter.py.

# Open the CupcakeInvoices.csv.
open_file = open('CupcakeInvoices.csv')
# Loop through all the data and print each row.
# for row  in open_file:
#     print(row)
# Loop through all the data and print the type of cupcakes purchased.
# for row  in open_file:
#     row = row.split(',')
#     print(row[2])
# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
# for row  in open_file:
#     row = row.split(',')
#     row[3] = float(row[3])
#     row[4] = float(row[4])
#     total = round((row[3] * row [4]), 2)
#     total = str(total)
#     print(total)
# Loop through all the data, and print out the total for all invoices combined.
total = 0
# for row  in open_file:
#     row = row.split(',')
#     row[3] = float(row[3])
#     row[4] = float(row[4])
#     total += row[3] * row [4]

# total = str(round(total, 2))
# print(total)
# Close your open file.
chocolate_count = 0
vanilla_count = 0
strawberry_count = 0
for row in open_file:
    row = row.split(',')
    if row[2] == 'Chocolate':
        chocolate_count += 1
    elif row[2] == 'Vanilla':
        vanilla_count += 1
    elif row[2] == 'Strawberry':
        strawberry_count += 1


open_file.close()
# Challenge: Do some research and see if you can limit your floats to never exceed two characters after the decimal point.

# Going Further
# Explore the graphing tools covered in today’s lecture. See if you can implement one of them to display the total income of chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.



import matplotlib.pyplot as plt

names = ['Chocolate', 'Vanilla', 'Strawberry']
values =[chocolate_count, vanilla_count, strawberry_count]

plt.figure(figsize=(9, 3))

plt.subplot(132)
plt.bar(names, values)
plt.suptitle('Cupcake popularity')
plt.show()