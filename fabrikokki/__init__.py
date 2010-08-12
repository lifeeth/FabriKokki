# FabriKokki init

from kokki.runner import Kokki
import kokki.providers

kokki = Kokki('config.yaml')

print "Here's your Kokki"
kokki._print()

fabrikokki = dict(
    File = "fabrikokki.providers.system.FileProvider",
    Directory = "fabrikokki.providers.system.DirectoryProvider",
    Link = "fabrikokki.providers.system.LinkProvider",
    Execute = "fabrikokki.providers.system.ExecuteProvider",
    Script = "fabrikokki.providers.system.ScriptProvider",
    Mount = "fabrikokki.providers.mount.MountProvider",
    User = "fabrikokki.providers.accounts.UserProvider",
),

# Just squirt our providers in there as if nothing happened
PROVIDERS['fabrikokki'] = fabrikokki

# Mutilate the kokki environment to force it to use our stuff
from kokki.environment import env
env.system.platform = "fabrikokki"
