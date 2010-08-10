import sys

try:
    from setuptools import setup
except ImportError:
    print "Please instal distribute from http://pypi.python.org/pypi/distribute"
    print "before installing FabriKokki."
    sys.exit(1)

from fabrikokki.version import get_version

README_CONTENTS = open("README").read()

setup(name='fabrikokki',
      version='0.1.0',
      author='Steve Steiner',
      author_email='ssteinerX@gmail.com',
      url='http://github.com/ssteinerX/FabriKokki/',
      download_url='http://github.com/ssteinerX/FabriKokki/',
      description='API between Fabric and Kokki.',
      long_description=README_CONTENTS,
      packages=find_packages(),
      provides=['fabrikokki'],
      keywords='fabric kokki chef puppet',
      license='BSD License',
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators',
                   'Environment :: Console',
                   'Natural Language :: English',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Unix',
                   'Operating System :: POSIX',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development',
                   'Topic :: Software Development :: Build Tools',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: System :: Clustering',
                   'Topic :: System :: Software Distribution',
                   'Topic :: System :: Systems Administration',
                  ],
        requires['fabric', 'kokki'],
     )
