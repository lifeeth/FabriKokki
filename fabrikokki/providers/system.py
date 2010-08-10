class DirectoryProvider(Provider):
    def action_create(self):
        path = self.resource.path
        if not fabric.contrib.files.exists(path, use_sudo=True, verbose=False):
            self.log.info("Creating directory %s" % self.resource)
            if self.resource.recursive:
                fabric.sudo('mkdir -p path ;' + 'chmod -R 755 ' + path)
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