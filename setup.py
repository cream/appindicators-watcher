from distutils.core import setup
from distutils.command.install_scripts import install_scripts

class post_install(install_scripts):

    def run(self):
        install_scripts.run(self)

        from shutil import move
        for i in self.get_outputs():
            n = i.replace('.py', '')
            move(i, n)
            print "moving '{0}' to '{1}'".format(i, n)


ID = 'org.cream.StatusNotifierWatcher'
data_files = [('share/cream/{0}'.format(ID), ['src/manifest.xml'])]


setup(
    name = 'cream-appindicators',
    version = '0.0.8',
    author = 'The Cream Project (http://cream-project.org)',
    url = 'http://github.com/cream/appindicators-watcher',
    package_dir = {'appindicators': 'src/appindicators'},
    packages = [
        'appindicators',
        'appindicators.dbusmenu',
        'appindicators.host',
        'appindicators.watcher'
    ],
    data_files = data_files,
    cmdclass={'install_scripts': post_install},
    scripts = ['src/appindicators-watcher.py']
)
