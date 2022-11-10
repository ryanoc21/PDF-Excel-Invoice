from excel_processing import File

file = File("invoices/*.xlsx")

if __name__ == '__main__':
    file.process()