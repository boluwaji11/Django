from django.shortcuts import render

# Create your views here.
def index(request):
    # The home page for Learning Log
    return render(request, "MainApp/index.html")


from .models import Topic


def topics(request):
    topics = Topic.objects.order_by("date_added")
    context = {"topic": topics}
    return render(request, "MainApp/topics.html", context)
