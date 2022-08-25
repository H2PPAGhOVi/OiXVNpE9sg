from django.http import HttpResponse

def show_misato(request):
    image_data = open("static/data.gif", "rb").read()
    return HttpResponse(image_data, content_type='image/gif')