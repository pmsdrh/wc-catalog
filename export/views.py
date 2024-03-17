from django.http import HttpResponse, JsonResponse
from django.template import loader
from wcapi.api import products
from django.views.decorators.csrf import csrf_exempt
from .jsonconvertor import excel, pdf


# Create your views here.


def export_excel(request):
    prd = products()
    prds = prd.show_all(keyword={"search": request.POST["excel-product-filter"]})
    exceljsonconvertor = excel(prds)
    exceljsonconvertor.json_to_excel()
    return HttpResponse("Ok")

@csrf_exempt
def export_pdf(request):
    print(request.POST)
    kw = request.POST["pdf-product-filter"]
    name = request.POST["pdf-name"]

    pdfjsonconvertor = pdf()
    ok = pdfjsonconvertor.json_to_pdf(kw, name)
    return JsonResponse({'success': ok[0], 'name': ok[1]})


def pdf_preview(request):
    prd = products()
    keyword = request.GET["f"]
    prds = prd.show_all(keyword={"search": keyword})
    template = loader.get_template('export/pdf.html')
    context = {"prds": prds}
    return HttpResponse(template.render(context, request))
