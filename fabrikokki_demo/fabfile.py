# August 10, 2010 -- ss
#
#   Just getting it all to run, not pulling in any of our provider
#   replacements.

from fabric.api import *

import kokki

import fabrikokki as fk

from kokki.runner import Kokki

fk.kokki = Kokki('config.yaml')

print "Here's your Kokki"
fk.kokki._print()


def _init_kokki(recipe_dir='./cookbooks'):
    """
    Initializes our Kokki instance

    TODO:   pull this out to the FabriKokki class and initialize that once we
            figure out what it has to do.
    """
    pass


def install_recipe(recipe, params):
    pass

_init_kokki()
