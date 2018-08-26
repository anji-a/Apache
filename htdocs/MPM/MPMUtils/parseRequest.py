


def parseRequest(request):

    for key in request.keys():
        if key.find('!') != -1:
            subdic = {}
            for subkey in key.split('!'):
                subdic

    tree_dict = {}
    for key in reversed(['k1', 'k2', 0, 'k3']):
        tree_dict = {key: tree_dict}

    print(tree_dict)
    print("parse Reqiest", request)
    return request