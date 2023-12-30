order_servers = ['http://order:5002', 'http://order2:5004']


def round_robin():
    global order_servers
    server = order_servers.pop(0)
    order_servers.append(server)
    return server
