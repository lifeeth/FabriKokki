from __future__ import with_statement

import grp
import os
import pwd
import subprocess
from kokki.base import Fail
from kokki.providers import Provider

class FileProvider(Provider):
    def action_create(self):
        path = self.resource.path
        write = False
        content = self._get_content()
        if not fabric.contrib.files.exists(path, use_sudo=True, verbose=False):
            write = True
            reason = "it didn't exist"
        else:
            #FIXME: add code for reading a remote file directly into a buffer
            #with open(path, "rb") as fp:
            #    old_content = fp.read()
            odl_content ="\/\/"
            if content != old_content:
                write = True
                reason = "contents didn't match"

        if write:
            self.log.info("Writing %s because %s" % (self.resource, reason))
            #with open(path, "wb") as fp:
            #    if content:
            #        fp.write(content)
            #FIXME: add code which writes directly to a buffer
            self.resource.updated()
        #FIXME: add alternative code which works over the network
        #stat = os.stat(self.resource.path)

        if self.resource.mode:
            #FIXME: fix this to work over the network
            #if stat.st_mode & 0777 != self.resource.mode:
            #    self.log.info("Changing permission for %s from %o to %o" % (self.resource, stat.st_mode & 0777, self.resource.mode))
            #    os.chmod(path, self.resource.mode)
            #    self.resource.updated()
            os.chmod(path, self.resource.mode)
            self.resource.updated()
        
        #FIXME: fix this to work over the network    
        #if self.resource.owner:
        #    try:
        #        new_uid = int(self.resource.owner)
        #    except ValueError:
        #        new_uid = pwd.getpwnam(self.resource.owner).pw_uid
        #    if stat.st_uid != new_uid:
        #        self.log.info("Changing owner for %s from %d to %s" % (self.resource, stat.st_uid, self.resource.owner))
        #        os.chown(path, new_uid, -1)
        
        #FIXME: make this work over the network
        #if self.resource.group:
        #    try:
        #        new_gid = int(self.resource.group)
        #    except ValueError:
        #        new_gid = grp.getgrnam(self.resource.group).gr_gid 
        #    if stat.st_gid != new_gid:
        #        self.log.info("Changing group for %s from %d to %s" % (self.resource, stat.st_gid, self.resource.group))
        #        os.chown(path, -1, new_gid)

    def action_delete(self):
        path = self.resource.path
        if fabric.contrib.files.exists(path, use_sudo=True, verbose=False):
            self.log.info("Deleting %s" % self.resource)
            fabric.sudo("rm %s" % path)
            self.resource.updated()

    def action_touch(self):
        path = self.resource.path
        fabric.sudo("touch %s" % path)

    #FIXME: make this work over the network
    #def _get_content(self):
    #    content = self.resource.content
    #    if isinstance(content, basestring):
    #        return content
    #    elif hasattr(content, "__call__"):
    #        return content()
    #    raise Fail("Unknown source type for %s: %r" % (self, content))

class DirectoryProvider(Provider):
    def action_create(self):
        path = self.resource.path
        if not fabric.contrib.files.exists(path, use_sudo=True, verbose=False):
            self.log.info("Creating directory %s" % self.resource)
            if self.resource.recursive:
                fabric.sudo('mkdir -p' +  path + ' ;' + 'chmod -R 755 ' + path)
            else:
                fabric.sudo('chmod 755 ' + path)
            self.resource.updated()

        #TODO fix this for fabric
        if self.resource.mode:
        #    stat = os.stat(path)
        #    if (stat.st_mode & 0777) != self.resource.mode:
        #        self.log.info("Changing permission for %s from %o to %o" % (self.resource, stat.st_mode & 0777, self.resource.mode))
        #        os.chmod(path, self.resource.mode)
        #        self.resource.updated()
            fabric.sudo('chmod -R ' + self.resource.mode + ' ' + path )

    def action_delete(self):
        path = self.resource.path
        if fabric.contrib.files.exists(path, use_sudo=True, verbose=False):
            self.log.info("Removing directory %s" % self.resource)
            if not path == '/':
                fabric.sudo('rm -rf ' + path)
                self.resource.updated()
                
class LinkProvider(Provider):
    def action_create(self):
        path = self.resource.path
        if fabric.contrib.files.exists(path, use_sudo=True, verbose=False):
            return

        if self.resource.hard:
            self.log.info("Creating hard %s" % self.resource)
            fabric.sudo('ln ' + self.resource.to + ' ' + path)
            self.resource.updated()
        else:
            self.log.info("Creating symbolic %s" % self.resource)
            fabric.sudo('ln -s ' + self.resource.to + ' ' + path)
            self.resource.updated()

    def action_delete(self):
        path = self.resource.path
        if os.path.exists(path):
            self.log.info("Deleting %s" % self.resource)
            fabric.sudo('unlink ' + path)
            self.resource.updated()
            

class ExecuteProvider(Provider):
    def action_run(self):
        if self.resource.creates:
            if fabric.contrib.files.exists(self.resource.creates, use_sudo=True, verbose=False):
                return

        self.log.info("Executing %s" % self.resource)
        #ret = subprocess.call(, shell=True, cwd=self.resource.cwd, env=self.resource.environment)
        #FIXME: fix the following code so that it also passes self.resource.environment
        with fabric.settings(fabric.hide('warnings','stdout','stderr', 'running'), warn_only=True):
            ret=fabric.sudo("cd %s ; %s" % (self.resource.cwd,  self.resource.command))

        if ret != self.resource.returns or ret.failed:
            raise Fail("%s failed, returned %d instead of %s" % (self, ret, self.resource.returns))
        self.resource.updated()

class ScriptProvider(Provider):
    def action_run(self):
        #FIXME: make this work on the remote host
        #from tempfile import NamedTemporaryFile
        #self.log.info("Running script %s" % self.resource)
        #with NamedTemporaryFile(prefix="kokki-script", bufsize=0) as tf:
        #    tf.write(self.resource.code)
        #    tf.flush()
        #    subprocess.call([self.resource.interpreter, tf.name], cwd=self.resource.cwd)