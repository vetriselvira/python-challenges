import requests
HOST_NAME = "http://192.168.1.110:8001"
DB_NAME = "student"


def console():
    requests.put("{}/{}".format(HOST_NAME,DB_NAME))
    # method = input("Enter your option")
    # if method == "add":
    #    db_name = input("Enter db_name")
    #   r = requests.put("{}/student".format("http://192.168.1.110:8001",db_name))
    while True:
        option = input("Enter your option 1. Insert 2.List\n")
        if option == "1":
            no_docs = input("Number of items to insert\n")
            print(no_docs)
            for i in range(int(no_docs)):
                name = input("Enter name\n")
                r = requests.post("{}/{}".format(HOST_NAME,DB_NAME),json={"name": name})
                rj = r.json()
                print(rj)
        elif option == "2":
            r = requests.get("{}/{}/_all_docs?include_docs=true".format(HOST_NAME,DB_NAME))
            rj = r.json()
            print(rj)
            print(rj["total_rows"])
            for item in rj["rows"]:
                if item['key'] != '_design/_views':
                    print(item['doc']['name'])
    # requests.delete("{}/{}".format(HOST_NAME, DB_NAME))


console()

