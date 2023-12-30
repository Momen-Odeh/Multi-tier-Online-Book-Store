catalog_servers = ['http://catalog:5001', 'http://catalog_replica:5003']


def round_robin():
    global catalog_servers
    server = catalog_servers.pop(0)
    catalog_servers.append(server)
    return server
