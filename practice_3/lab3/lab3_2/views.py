from genericpath import isfile
import os
from lab3.settings import TEMPLATE_DIRS
from django.http import HttpResponse


def get_content(request):
    html = "<html><body>"
    try:
        html += "<b>Files in catalogue is</b> %s" % files_in_catalogue(request)
    except:
        html += "<t1><b>No such folder</b></t1>"
    html += "</body></html>"
    return HttpResponse(html)


def get_directory(request):
    return TEMPLATE_DIRS + request.get_full_path()


def get_folder_html(file, request):
    return r"<br><a href=" + request.get_full_path() + "/" + file + ">" + file + "</a>"


def files_in_catalogue(request):
    files_list = ""
    current_dir = get_directory(request)
    os.chdir(current_dir)
    for file in os.listdir("."):
        if isfile(file):
            files_list += '<br>' + file
        else:
            files_list += get_folder_html(file, request)
    return files_list
