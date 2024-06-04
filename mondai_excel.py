from openpyxl import Workbook

# Create a new workbook
wb = Workbook()

# Select the active sheet
sheet = wb.active






# Sample numerical data
"""data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Insert data into range B2:E5
for row_idx, row_data in enumerate(data, start=2):
    for col_idx, cell_value in enumerate(row_data, start=2):
        sheet.cell(row=row_idx, column=col_idx, value=cell_value)


# Specify the range of cells (B2:E5)
cell_range = sheet['B2:E5']

# Calculate the average value of the specified range
average_value = "=AVERAGE({})".format(cell_range)

# Insert the average formula into a cell
sheet['B9'] = average_value

# Calculate the total value (sum) of the specified range
total_value = "=SUM({})".format(cell_range)

# Insert the total formula into a cell
sheet['C9'] = total_value

# Save the workbook
wb.save('example.xlsx')"""




