import csv , xlrd

def csv_converter(path , name):

    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_name(name)
    with open('output.csv' , 'w' , encoding = 'utf8') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)

        for row in range(sh.nrows):
            wr.writerow(sh.row_values(row))


path = '/Users/chegreyev/Downloads/Telegram Desktop/documentation_table.xlsx'
name = 'Practise'

if __name__ == "__main__":
    path = '/Users/chegreyev/Desktop/output.xlsx'
    name = 'Practise'

    csv_converter(path , name)