
from kokki import *
from os.path import exists

def nginx_site(name, enable=True):
    if enable:
        cmd = 'nxensite'
    else:
        cmd = 'nxdissite'

    Execute("%s %s" % (cmd,name),
            command = "/usr/sbin/%s %s" % (cmd,name),
            notifies = [("reload", env.resources["Service"]["nginx"])],
            not_if = lambda:exists("%s/sites-enabled/%s" % (env.nginx.dir, name)))

def setup():
    # TODO: ss -- if there's a reason to check env.system.platform, then the
    #             else branch should do something different.  The metadata.yaml
    #             specifically only calls out debian and ubuntu as supported
    #             platforms anyway.
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
