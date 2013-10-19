import time
from genericpath import isfile
import os
from lab3.settings import TEMPLATE_DIRS
from django.http import HttpResponse


def get_content(request):
    html = "<html><body>"
    try:
        html += "<b>Files in catalogue is</b> %s" % files_in_catalogue(request)
    except FileNotFoundError:
        html += "no such directory"
    html += "</body></html>"
    return HttpResponse(html)


def get_directory(request):
    return TEMPLATE_DIRS + request.get_full_path()


def folder_to_url(file, req):
    html_str = file
    if not isfile(file):
        html_str = "<a href=" + req.get_full_path() + "/" + file + ">" + file + "</a>"
    return html_str


def get_mtime(current_dir, file):
    mtime = os.stat(current_dir + "/" + file).st_mtime
    gmtime = time.gmtime(mtime)
    return time.strftime("%m/%d/%Y %H:%M:%S", gmtime)


def get_size(current_dir, file):
    return str(os.stat(current_dir + "/" + file).st_size)


def get_file_info(current_dir, file, request):
    attribs = [
        folder_to_url(file, request),
        get_size(current_dir, file),
        get_mtime(current_dir, file)]
    table_row = add_td(attribs)
    return table_row


def add_td(cells):
    newcells = ""
    for cell in cells:
        newcells += "<td>" + cell + "</td>"
    return newcells


def files_in_catalogue(request):
    files_list = "<table border=1>"
    current_dir = get_directory(request)
    os.chdir(current_dir)
    for file in os.listdir("."):
        files_list += "<tr>" + get_file_info(current_dir, file, request) + "</tr>"
    files_list += "</table>"
    return files_list
