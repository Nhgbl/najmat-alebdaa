import os
import sys
import django
sys.path.append('e:/Najmat_Alibdaa')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.test import Client
c = Client()
try:
    response = c.get('/about/')
    print('Status:', response.status_code)
except Exception as e:
    import traceback
    traceback.print_exc()
