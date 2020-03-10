from app import db
from app.models.tables import Atividade
from datetime import date

a1 = Atividade(nome='Oficina Git Hub', tipo='Oficina', data=date(2020, 3, 9), carga_horaria=8, arquivo='/09032020/1.pdf', usuario_id=1)
a2 = Atividade(nome='Palestra Bit Data', tipo='Palestra', data=date(2020, 3, 9), carga_horaria=1, arquivo='/09032020/2.pdf', usuario_id=1)
a3 = Atividade(nome='Oficina Jekyll', tipo='Oficina', data=date(2020, 3, 9), carga_horaria=10, arquivo='/09032020/3.pdf', usuario_id=1)

db.session.add(a1)
db.session.add(a2)
db.session.add(a3)

db.session.commit()
