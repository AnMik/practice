# -*- coding: utf-8 -*-
dict = {}

def initdictionary():
    dict.clear()
    with open("hosts.txt") as f:
        for host in f.readlines():
            if host.rstrip():
                (address, name) = host.replace('\n', '').split(' ')
            dict[name] = address

def showhosts():
    initdictionary()
    print dict.items()

def addnewhost():
    ip = raw_input("Enter IP\n")
    name = raw_input("Enter Name\n")
    with open("hosts.txt", "a") as f:
        f.write("\n" + ip + " " + name)
    print "'" + ip + ' ' + name + "' added"

def searchfromname():
    initdictionary()
    found = False
    namesearch = raw_input("Enter name\n")
    for name, ip in dict.iteritems():
        if name.startswith(namesearch):
            print(name + ' ' + ip)
            found = True
    if not found:
        print("No such name in host file")

def searchfromip():
    initdictionary()
    found = False
    ipsearch = raw_input("Enter ip\n")
    for name, ip in dict.iteritems():
        if ip.startswith(ipsearch):
            print(ip + ' ' + name)
            found = True
    if not found:
        print("No such ip in host file")

def search():
    type = raw_input("Name or IP or Exit?\n")
    if type.lower().startswith("n"):
        searchfromname()
        search()
    elif type.lower().startswith("i"):
        searchfromip()
        search()
    elif type.lower().startswith("e"):
        startinput()
    else:
        print("Unknown command")
        search()

def startinput():
    inputstr = raw_input(
        "Enter 'Add' for add new server, 'Show' to see host-file, 'Search' for find host or 'Exit' for finish this\n")
    if inputstr.lower().startswith("e"):
        print "Finished this"
    elif inputstr.lower().startswith("sh"):
        showhosts()
        startinput()
    elif inputstr.lower().startswith("se"):
        search()
    elif inputstr.lower().startswith("a"):
        addnewhost()
        startinput()
    else:
        print("Unknown command")
        startinput()

def main():
    try:
        startinput()
    except:
        print "Something wrong"
        startinput()

main()