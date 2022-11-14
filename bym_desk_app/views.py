from django.http import JsonResponse

def createUser(request):
    # if request.method == 'POST':
    user = {'id': 1}
    return JsonResponse(user)
