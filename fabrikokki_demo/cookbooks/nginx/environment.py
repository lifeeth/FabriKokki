# TODO: is this even necessary?  Exact same thing is done in
#       recipes/default.py's setup() function, this looks like a leftover
if env.system.platform in ("debian", "ubuntu"):
    env.nginx.dir     = "/etc/nginx"
    env.nginx.log_dir = "/var/log/nginx"
    env.nginx.user    = "www-data"
    env.nginx.binary  = "/usr/sbin/nginx"
else:
    env.nginx.dir     = "/etc/nginx"
    env.nginx.log_dir = "/var/log/nginx"
    env.nginx.user    = "www-data"
    env.nginx.binary  = "/usr/sbin/nginx"
