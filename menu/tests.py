import re

from django.test import TestCase

# Create your tests here.
requested_url = 'dasd/sad'
match = re.findall(r"/(.*?)/", requested_url)

print(match[-1])