import json
import platform
import sys

if platform.system() != 'Linux':
    print "Currently only Linux platforms supported."
    sys.exit(2)

os = dict(zip(['distro', 'version', 'codename'],list(platform.dist())))

print(json.dumps(os))
