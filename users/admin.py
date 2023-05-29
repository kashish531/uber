from django.contrib import admin

# Register your models here.
from users.models import (Student,)
admin.site.register(Student)
from users.models import (Orders,)
admin.site.register(Orders)
from users.models import (StudentsAddress)
admin.site.register(StudentsAddress)
