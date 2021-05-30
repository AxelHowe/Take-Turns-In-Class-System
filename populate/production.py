from populate import base
from user.models import User

print('Creating admin account ... ', end='')
User.objects.create_superuser(username='admin', password='87z632xx87', email=None,)
print('done')