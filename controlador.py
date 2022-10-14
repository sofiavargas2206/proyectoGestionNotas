import sqlite3

def validar_usuario(usuario, password):
    db=sqlite3.connect("BaseNotas.db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select * from usuario where usuario='"+usuario+"' and contraseña='"+password+"' "
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    return resultado

def lista_destinatarios(usuario):
    db=sqlite3.connect("BaseNotas.db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select *from usuario where usuario<>'"+usuario+"' "
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    return resultado
