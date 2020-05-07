


def converttopdf(filename):
    import pdfkit
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    url = "index.html"
    pdfkit.from_file(filename, '{}.pdf'.format(filename), configuration=config)



if __name__ == '__main__':
    print(converttopdf('../convertpdf/index.html'))
