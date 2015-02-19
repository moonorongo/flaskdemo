# -*- coding: iso-8859-1 -*-
from sqlalchemy import create_engine
import fdb

# FORMA SIMPLE ACCESO A DB

# con = fdb.connect(dsn='/threads/proyectos/academia/db/ACADEMIA.DB', user='SYSDBA', password='masterkey')
# cur = con.cursor()
# cur.execute("SELECT CODIGO, NOMBRE FROM UBICACIONES")
# print(cur.fetchall())



engine = create_engine('firebird+fdb://sysdba:masterkey@localhost:3050/ACADEMIA')    
