from http.server import HTTPServer,ThreadingHTTPServer, SimpleHTTPRequestHandler
from gen_feed import gen_feed
import logging.config , os


LOG_CONF='logging.ini'
if os.path.exists(LOG_CONF): logging.config.fileConfig(LOG_CONF) 


PORT = int(os.getenv('PORT')) or 8000
HOST = os.getenv('HOST') or 'localhost'
ENDPOINT = os.getenv('ENDPOINT') or  'http://%s:%s' %(HOST, PORT)

gen_feed(ENDPOINT)


# Creates a really basic server the serves this entire directory
def run(server_class=ThreadingHTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print('Starting server at ' + ENDPOINT)
    httpd.serve_forever()


run()
