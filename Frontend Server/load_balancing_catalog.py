catalog_servers = ['http://localhost:5001', 'http://localhost:5002']


def round_robin():
    global catalog_servers
    server = catalog_servers.pop(0)
    catalog_servers.append(server)
    return server
