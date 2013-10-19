import time
from genericpath import isfile
import os
from django.shortcuts import render
from lab3.settings import TEMPLATE_DIRS
from django.http import HttpResponse


def get_content(request):
    try:
        rows = get_rows(request)
    except FileNotFoundError:
        return HttpResponse("No such directory")
    return render(request, "listing.html", {'rows': rows})


def get_rows(request):
    files_list = []
    current_dir = get_directory(request)
    os.chdir(current_dir)
    for file in os.listdir("."):
        files_list.append(get_file_info(current_dir, file, request))
    return files_list


def get_directory(request):
    return TEMPLATE_DIRS + request.get_full_path()


def folder_to_url(file, req):
    html_str = file
    if not isfile(file):
        html_str = "<a href=\"" + req.get_full_path() + "/" + file + "\">" + file + "</a>"
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
    return attribs
