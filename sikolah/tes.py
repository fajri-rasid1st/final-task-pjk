from sikolah import db
from sikolah.models import *

data = User.query.get(1).data_user.data_siswa

for i in data:
    print(data[i])
