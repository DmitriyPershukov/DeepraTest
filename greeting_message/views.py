from django.http import HttpResponse


def index(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
    response = ""
    if (name is None):
        response += "Parameter name was not provided."
    if (message is None):
        response += "Parameter message was not provided."
    if (response == ""):
        response = "Hello {}! {}!".format(name, message)
    return HttpResponse(response)