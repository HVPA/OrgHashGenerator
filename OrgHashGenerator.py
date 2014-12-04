import sys, os, hashlib, string, random

from django.core.management import setup_environ

# path where Portal django app is located, this usually 1 directory up from 
# where the app sits. e.g: '/path/location/Portal' then put down '/path/location'
path = '/path/location'
sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Portal.settings'

from Portal import settings
setup_environ(settings)

from Portal.hvp.models.search.Organisation import Organisation

def GenerateHash():
    # first generate random string
    randomStr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))

    # generate md5 hash using the random string generated
    md5hash = hashlib.md5()
    md5hash.update(randomStr)

    return md5hash.hexdigest()


# generate hash
org_hash = GenerateHash()

# loop to check if hash exist in db, keep generating hash until 
# we get a unique hash 
skip = False
while not skip:
    if Organisation.objects.filter(HashCode=org_hash):
        org_hash = GenerateHash()
    else:
        skip = True

print org_hash
