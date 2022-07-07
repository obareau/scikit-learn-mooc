from __future__ import print_function
from distutils.version import LooseVersion as Version
import sys

OK = '\x1b[42m[ OK ]\x1b[0m'
FAIL = "\x1b[41m[FAIL]\x1b[0m"

try:
    import importlib
except ImportError:
    print(FAIL, "Python version 3.6 or above is required,"
                " but %s is installed." % sys.version)


def import_version(pkg, min_ver, fail_msg=""):
    mod = None
    try:
        mod = importlib.import_module(pkg)
        if pkg in {'PIL'}:
            try:
                ver = mod.__version__
            except AttributeError:
                try:
                    ver = mod.VERSION
                except AttributeError:
                    try:
                        ver = mod.PILLOW_VERSION
                    except:
                        raise
        else:
            ver = mod.__version__
        if Version(ver) < min_ver:
            print(
                FAIL,
                f"{lib} version {min_ver} or higher required, but {ver} installed.",
            )

        else:
            print(OK, f'{pkg} version {ver}')
    except ImportError:
        print(FAIL, f'{pkg} not installed. {fail_msg}')
    return mod


# first check the python version
print('Using python in', sys.prefix)
print(sys.version)
pyversion = Version(sys.version)
if (
    pyversion >= "3"
    and pyversion < "3.6"
    or pyversion < "3"
    and pyversion >= "2"
):
    print(FAIL, "Python version 3.6 or above is required,"
                " but %s is installed." % sys.version)
elif pyversion < "3":
    print(FAIL, f"Unknown Python version: {sys.version}")

print()
requirements = {'numpy': "1.16", 'scipy': "1.2", 'matplotlib': "3.0",
                'sklearn': "1.1", 'pandas': "1",
                'seaborn': "0.11",
                'notebook': "5.7", 'plotly': "4.3"}

# now the dependencies
for lib, required_version in list(requirements.items()):
    import_version(lib, required_version)
