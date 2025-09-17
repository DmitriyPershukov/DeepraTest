from django.http import HttpResponse


def index(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
    response = ""
    if (name is None):
        response += "<p>Parameter name was not provided.</p>"
    if (message is None):
        response += "<p>Parameter message was not provided.</p>"
    if (response == ""):
        response = "<p>Hello {}! {}!</p>".format(name, message)
    return HttpResponse(response)