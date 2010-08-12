# FabriKokki init

from kokki.runner import Kokki
import kokki.providers

# A dictionary of implementations for each of the providers
fabrikokki = dict(
    File = "fabrikokki.providers.system.FileProvider",
    Directory = "fabrikokki.providers.system.DirectoryProvider",
    Link = "fabrikokki.providers.system.LinkProvider",
    Execute = "fabrikokki.providers.system.ExecuteProvider",
    Script = "fabrikokki.providers.system.ScriptProvider",
    Mount = "fabrikokki.providers.mount.MountProvider",
    User = "fabrikokki.providers.accounts.UserProvider",
)

class FabriKokki(Kokki):
    def __init__(self, config):
        super(FabriKokki,self).__init__(config)

        print "fk.__init__, Here's your Kokki"
        self._print()

        # Just squirt our providers in there as if nothing happened
        kokki.providers.PROVIDERS['fabrikokki'] = fabrikokki

        # Mutilate the kokki environment to force it to use our stuff
        # I'm (ss) pretty sure the environment is bound during actual execution
        from kokki.environment import env
        env.set_attributes( {'system.platform':'fabrikokki'} )

    # These are the other methods...
    # ------------------------------
    # load_cookbooks(self):
    # run_action(self, resource, action):
    # _check_condition(self, cond):
    # run_roles(self, roles):
    # __str__(self):
    # _print(self):
