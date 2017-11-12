from http.server import HTTPServer, SimpleHTTPRequestHandler
from gen_feed import gen_feed

PORT = 8000
HOST = 'http://localhost:' + str(PORT)

gen_feed(HOST)


# Creates a really basic server the serves this entire directory
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print('Starting server at ' + HOST)
    httpd.serve_forever()


run()
