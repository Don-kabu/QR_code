from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Document,Scan
from .utils import get_client_ip,insert_qr_pdf
from .forms import ScanForm,DocumentForm
from django.http import HttpResponse
from django.utils.text import slugify

# Create your views here.



@csrf_exempt
def log_scan(request):
    data = json.loads(request.body)
    document = Document.objects.get(unique_id=data['qr_label'])
    scan = Scan.objects.create(
        document=document,
        ip_address=get_client_ip(request),
        latitude=data.get('latitude'),
        longitude=data.get('longitude'),
        user_agent=request.META.get('HTTP_USER_AGENT')
    )
    return JsonResponse({"status": "ok"})








def create_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            document_name = form.cleaned_data['file']
            insert_qr_pdf(str(slugify(document_name))[:-4],form.cleaned_data['unique_id'])
            return HttpResponse(str(document_name))
    else:
        form = DocumentForm()
    return render(request, "create_document.html", {"form": form})



























# def create_scan(request):
#     if request.method == "POST":
#         form = ScanForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = ScanForm()
#     return render(request, "create_scan.html", {"form": form})
