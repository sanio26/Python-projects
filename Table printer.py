print("Sanio Frederic,1AY24AI099,SEC-O")
def print_table(table_data):
    # Determine the width of each column
    col_widths = [max(len(item) for item in col) for col in table_data]
    num_rows = len(table_data[0])

    for row in range(num_rows):
        for col in range(len(table_data)):
            print(table_data[col][row].rjust(col_widths[col]), end=' ')
        print()

# Sample table data (each sublist is a column)
table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

if __name__ == "__main__":
    print_table(table_data)
