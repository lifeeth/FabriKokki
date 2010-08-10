from __future__ import with_statement
import re
import grp
import fabric
from kokki.base import Fail
from kokki.providers import Provider

class UserProvider(Provider):
    def action_create(self):
        if not self.user:
            command = ['useradd']

            useradd_options = dict(
                comment = "-c",
                gid = "-g",
                uid = "-u",
                shell = "-s",
                password = "-p",
            )

            for option_name, option_value in self.resource.arguments.items():
                option_flag = useradd_options.get(option_name)
                if option_flag:
                    command += [option_flag, option_value]
                    
            command.append(self.resource.username)

            fabric.sudo(command)
            self.resource.updated()

    @property
    def user(self):
        with fabric.settings(fabric.hide('warnings','stdout','stderr', 'running'), warn_only=True):
            res=fabric.sudo('grep "^%s:" /etc/passwd' % self.resource.username)
        if res.failed:
            return None