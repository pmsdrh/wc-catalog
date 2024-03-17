from django.urls import path

from .views import export_excel, export_pdf, pdf_preview

urlpatterns = [
    path('excel/', export_excel),
    path('pdf/', export_pdf),
    path('pdf/preview/', pdf_preview, name="pdf_preview")
]
