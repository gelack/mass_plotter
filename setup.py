

######################################################################################
#
# YOU CAN / SHOULD EDIT THE FOLLOWING SETTING
#
######################################################################################

PKG_NAME = 'mass_plotter'

VERSION = (0, 0, 1)

# list all required packages here:

REQUIRED_PACKAGES = []


### install package as emzed extension ? #############################################
#   -> package will appear in emzed.ext namespace after installation

IS_EXTENSION = True


### install package as emzed app ?  ##################################################
#   -> can be started as app.mass_plotter()
#   set this variable to None if this is a pure extension and not an emzed app

APP_MAIN = "mass_plotter.app:run"


### author information ###############################################################

AUTHOR = 'Gerald Lackner'
AUTHOR_EMAIL = 'gerald.lackner@uni-jena.de'
AUTHOR_URL = ''


### package descriptions #############################################################

DESCRIPTION = "please describe here mass_plotter in one line"
LONG_DESCRIPTION = """

describe mass_plotter here in more than one line

"""

LICENSE = "http://opensource.org/licenses/GPL-3.0"


######################################################################################
#                                                                                    #
# DO NOT TOUCH THE CODE BELOW UNLESS YOU KNOW WHAT YOU DO !!!!                       #
#                                                                                    #
#                                                                                    #
#       _.--""--._                                                                   #
#      /  _    _  \                                                                  #
#   _  ( (_\  /_) )  _                                                               #
#  { \._\   /\   /_./ }                                                              #
#  /_"=-.}______{.-="_\                                                              #
#   _  _.=('""')=._  _                                                               #
#  (_'"_.-"`~~`"-._"'_)                                                              #
#   {_"            "_}                                                               #
#                                                                                    #
######################################################################################


VERSION_STRING = "%s.%s.%s" % VERSION

ENTRY_POINTS = dict()
ENTRY_POINTS['emzed_package'] = [ "package = " + PKG_NAME, ]
if IS_EXTENSION:
    ENTRY_POINTS['emzed_package'].append("extension = " + PKG_NAME)
if APP_MAIN is not None:
    ENTRY_POINTS['emzed_package'].append("main = %s" % APP_MAIN)


if __name__ == "__main__":   # allows import setup.py for version checking

    from setuptools import setup
    setup(name=PKG_NAME,
        packages=[ PKG_NAME ],
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=AUTHOR_URL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        version=VERSION_STRING,
        entry_points = ENTRY_POINTS,
        install_requires = REQUIRED_PACKAGES,
        )
   