order_servers = ['http://localhost:5002', 'http://localhost:5002']  # 5002 5004


def round_robin():
    global order_servers
    server = order_servers.pop(0)
    order_servers.append(server)
    return server
