import os

import jdatetime as jdt
import pdfkit
from django.conf import settings
from openpyxl import Workbook


class excel:
    def __init__(self, products_json):
        self.products_json = products_json

    def json_to_excel(self):
        workbook = Workbook()
        sheet = workbook.active
        sheet.sheet_view.rigtToleft = True

        sheet["A1"] = "ردیف"
        sheet["B1"] = "نام"
        sheet["C1"] = "قیمت"
        sheet["D1"] = "طول"
        sheet["E1"] = "عرض"
        sheet["F1"] = "ارتفاع"
        a = 2
        for i in self.products_json:
            sheet["A" + str(a)] = a - 1
            sheet["B" + str(a)] = i["name"]
            sheet["C" + str(a)] = i["regular_price"]
            sheet["D" + str(a)] = i["dimensions"]["length"]
            sheet["E" + str(a)] = i["dimensions"]["width"]
            sheet["F" + str(a)] = i["dimensions"]["height"]
            a += 1

        workbook.save(filename=os.path.join(settings.STATICFILES_DIRS[0], 'download\\excel\\Hi.xlsx'))


class pdf:
    def json_to_pdf(self, kw, name):
        config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
        options = {'page-size': 'A4',
                   'margin-top': '0.75in',
                   'margin-right': '0.75in',
                   'margin-bottom': '0.75in',
                   'margin-left': '0.75in',
                   'encoding': "UTF-8",
                   }
        pdf_name = '{}-{}.pdf'.format(name, str(jdt.date.today()))
        return (pdfkit.from_url("http://127.0.0.1:8000/export/pdf/preview/?f={}".format(kw),
                               os.path.join(settings.STATICFILES_DIRS[0],
                                            'download\\pdf\\{}'.format(pdf_name)),
                               configuration=config, options=options), pdf_name)
