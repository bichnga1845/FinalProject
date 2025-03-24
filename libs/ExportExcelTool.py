import xlsxwriter as xr

class ExportImportExcelTool:

    def export_reader_excel(self,readers,filename):
        # export cai gi (categories) vao dau (filename)
        workbook = xr.Workbook(filename)
        worksheet = workbook.add_worksheet()

        # modify column width
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:C', 20)
        worksheet.set_column('D:D', 20)
        worksheet.set_column('E:E', 20)
        worksheet.set_column('F:F', 20)
        worksheet.set_column('G:G', 20)

        bold = workbook.add_format({'bold': True})

        # add header
        worksheet.write('A1', 'Reader ID', bold)
        worksheet.write('B1', 'Reader Name', bold)
        worksheet.write('C1', 'Gender', bold)
        worksheet.write('D1', 'Date of Birth', bold)
        worksheet.write('E1', 'Phone', bold)
        worksheet.write('F1', 'Address', bold)
        worksheet.write('G1', 'Books', bold)

        for i in range(len(readers)):
            index = i + 2
            obj = readers[i]
            worksheet.write(f'A{index}', obj.reader_id)
            worksheet.write(f'B{index}', obj.name)
            worksheet.write(f'C{index}', obj.gender)
            worksheet.write(f'D{index}', obj.date)
            worksheet.write(f'E{index}', obj.phone)
            worksheet.write(f'F{index}', obj.address)
            worksheet.write(f'G{index}', ", ".join(f"{book_id} (x{quantity})" for book_id, quantity in obj.books))
        workbook.close()

    def export_book_excel(self, books, filename):
        workbook = xr.Workbook(filename)
        worksheet = workbook.add_worksheet()

        # modify column width
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:C', 20)
        worksheet.set_column('D:D', 20)
        worksheet.set_column('E:E', 20)
        worksheet.set_column('F:F', 20)
        worksheet.set_column('G:G', 20)
        worksheet.set_column('H:H', 20)

        bold = workbook.add_format({'bold': True})

        # add header
        worksheet.write('A1', 'Book ID', bold)
        worksheet.write('B1', 'Book Name', bold)
        worksheet.write('C1', 'Book Type', bold)
        worksheet.write('D1', 'Published Date', bold)
        worksheet.write('E1', 'Publisher', bold)
        worksheet.write('F1', 'Price', bold)
        worksheet.write('G1', 'Quantity', bold)
        worksheet.write('H1', 'Author', bold)

        for i in range(len(books)):
            index = i + 2
            obj = books[i]
            worksheet.write(f'A{index}', obj.book_id)
            worksheet.write(f'B{index}', obj.book_name)
            worksheet.write(f'C{index}', obj.type)
            worksheet.write(f'D{index}', obj.published_year)
            worksheet.write(f'E{index}', obj.publisher)
            worksheet.write(f'F{index}', obj.price)
            worksheet.write(f'G{index}', obj.quantity)
            worksheet.write(f'H{index}', obj.author)
        workbook.close()
    def export_author_excel(self,authors,filename):
        workbook = xr.Workbook(filename)
        worksheet = workbook.add_worksheet()

        # modify column width
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:C', 20)
        worksheet.set_column('D:D', 20)
        worksheet.set_column('E:E', 20)
        worksheet.set_column('F:F', 50)

        bold = workbook.add_format({'bold': True})

        # add header
        worksheet.write('A1', 'Author ID', bold)
        worksheet.write('B1', 'Author Name', bold)
        worksheet.write('C1', 'Gender', bold)
        worksheet.write('D1', 'Hometown', bold)
        worksheet.write('E1', 'Book Counts', bold)
        worksheet.write('F1', 'Books', bold)

        for i in range(len(authors)):
            index = i + 2
            obj = authors[i]
            worksheet.write(f'A{index}', obj.author_id)
            worksheet.write(f'B{index}', obj.name)
            worksheet.write(f'C{index}', obj.gender)
            worksheet.write(f'D{index}', obj.hometown)
            worksheet.write(f'E{index}', len(obj.books))
            worksheet.write(f'F{index}', ", ".join(book for book in obj.books))

        workbook.close()
    def export_order_excel(self,orders, filename):
        workbook = xr.Workbook(filename)
        worksheet = workbook.add_worksheet()

        # modify column width
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:C', 20)
        worksheet.set_column('D:D', 20)
        worksheet.set_column('E:E', 20)
        worksheet.set_column('F:F', 20)
        worksheet.set_column('G:G', 20)

        bold = workbook.add_format({'bold': True})

        # add header
        worksheet.write('A1', 'Order ID', bold)
        worksheet.write('B1', 'Reader ID', bold)
        worksheet.write('C1', 'Book ID', bold)
        worksheet.write('D1', 'Quantity', bold)
        worksheet.write('E1', 'Status', bold)
        worksheet.write('F1', 'Borrowing Date', bold)
        worksheet.write('G1', 'Returning Date', bold)

        for i in range(len(orders)):
            index = i + 2
            obj = orders[i]
            worksheet.write(f'A{index}', obj.order_id)
            worksheet.write(f'B{index}', obj.reader_id)
            worksheet.write(f'C{index}', obj.book_id)
            worksheet.write(f'D{index}', obj.quantity)
            worksheet.write(f'E{index}', obj.status)
            worksheet.write(f'F{index}', obj.borrow_date)
            worksheet.write(f'G{index}', obj.return_date)

        workbook.close()
