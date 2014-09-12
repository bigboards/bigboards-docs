#!/usr/bin/env python
from livereload import Server, shell

server = Server()

# watch docs to compile
server.watch('docs/', shell('make html'))

# watch html to serve
server.watch('build/html/')

# serve the server and open the URL
server.serve(open_url=True)

# live preview of sphynx docx according to http://serialized.net/2013/01/live-sphinx-documentation-preview/
# but livereload evolved in the mean time http://livereload.readthedocs.org/en/latest/
# and example at https://github.com/lepture/python-livereload/blob/master/example/server.py

# To run this utilty, you have to install pip via either 'brew install pip' or 'easy_install pip'.
# Next you have to install LiveReload via 'pip install livereload'
