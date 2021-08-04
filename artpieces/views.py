from typing import Text
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Artist
import datetime

# Create your views here.
def home(request):
    today = datetime.datetime.now().date()
    return render(request, "index.html", {"today" : today})

def login_reg(request):
    return render(request, "login_reg.html", {})

def detail(request, number_id):
    text = ("<h2>Details for Album id:" + str(number_id) + "</h2> ")
    return HttpResponse(text)

def index(request):
    all_artists = Artist.objects.all() #imports all albums from the database
    # html = ''
    # for album in all_albums:
    # 	url = '/music/' + str(album.id) + '/'
    # 	html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    template = loader.get_template('index.html')
    context = {
	    'all_artists': all_artists
	}

    return HttpResponse(template.render(context, request))

#def detail(request, album_id):
#	return HttpResponse("<h1>Welcome to my app number %s!<h1>")