from kokki import *

Package("apache2")
File("/etc/apache2/ports.conf",
    owner = "www-data",
    content = "Listen %d\n" % env.example.web_port)