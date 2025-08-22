from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Document,Scan
from .utils import get_client_ip,insert_qr_pdf,send_document_notification
from .forms import DocumentForm
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



def home(request):
    return render(request, "home.html")




def create_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            document_name = form.cleaned_data['file']
            id = Document.objects.last()
            return_link = insert_qr_pdf(str(document_name)[:-4],id=id.unique_id)
            
        #     send_document_notification(
        #     to_email='kabudon19@gmail.com',
        #     to_phone='+243892649177',
        #     document_label=id.label,
        #     document_url= ""
        # )

            return HttpResponse(f"<a href='{return_link}'> download<a/>")
    else:
        form = DocumentForm()
    return render(request, "create_document.html", {"form": form})


def document_list(request):
    documents = Document.objects.all()
    return render(request, "document_list.html", {"documents": documents})



def visit_link(request,id):
    # try:
    document = Document.objects.get(unique_id=id)
    print(document)
    send_document_notification(
        to_email='kabu.d@calculus-system.net',
        to_phone='+243892268023',
        document_label=document.label,
        document_url="ok"
    )

    print("""





ok
""")
    # except:
    #     return HttpResponse("does not exist")
    return redirect("http://www.google.com")























# def create_scan(request):
#     if request.method == "POST":
#         form = ScanForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = ScanForm()
#     return render(request, "create_scan.html", {"form": form})
