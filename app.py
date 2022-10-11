from ast import Not
from asyncio.windows_events import NULL
from operator import not_
from flask import Flask,render_template,request,redirect,url_for,flash
from datetime import datetime
import sqlite3 as sql

app=Flask(__name__)
app.secret_key='admin123'

@app.route('/')


@app.route('/Inicio')
def Inicio():
      return render_template('Inicio.html')


@app.route('/Estudiante')
def Estudiante():
   
    con=sql.connect('BaseNotas.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from persona where estado="Activo" and idRol=1')
    data=cur.fetchall()
    return render_template('Estudiante.html',datas=data)

@app.route('/consultaEstudiante',methods=['GET','POST'])
def consultaEstudiante():      
    if request.method == 'POST':
        documentoFiltro=request.form['documentoFiltro']
        nombres=request.form['nombresFiltro']
        con=sql.connect('BaseNotas.db')
        con.row_factory=sql.Row
        cur=con.cursor()
        if documentoFiltro !='' or nombres!='':
            cur.execute('select * from persona WHERE identificacion=? or nombres=? and estado="Activo" and idRol=1',(documentoFiltro,nombres) )
           
        else:
            cur.execute('select * from persona where idRol=1')  
           
        data=cur.fetchall()
    return render_template('Estudiante.html',datas=data)

@app.route('/addPersona',methods=['GET','POST'])
def addPersona():
    if request.method=='POST':
        nombres=request.form['nombresPersona']
        apellidos=request.form['apellidosPersona']
        tipoDocumento=request.form['tipoDocumentoPersona']
        documento=request.form['identificacionPersona']
        correo=request.form['correoPersona']
        telefono=request.form['telefonoPersona']
        idRol=request.form['rolPersona']
        fechaRegistro= datetime.now()
        fechaActualizacion= datetime.now()
        estado='Activo'
        con=sql.connect('BaseNotas.db')
        cur=con.cursor()
        cur.execute('insert into persona (nombres,apellidos,tipoIdentificacion,identificacion,telefono,email,fechaRegistro,fechaActualizacion,idRol,estado) values (?,?,?,?,?,?,?,?,?,?)',(nombres,apellidos,tipoDocumento,documento,telefono,correo,fechaRegistro,fechaActualizacion,idRol,estado))
        con.commit()
        flash('Usuario Guardado','success')
        return redirect(url_for('Estudiante'))
    return render_template('Estudiante.html')

@app.route('/editPersona/<string:idPersona>',methods=['GET','POST'])
def editPersona(idPersona):
    if request.method == 'POST':
        
        con=sql.connect('BaseNotas.db')
        con.row_factory=sql.Row
        error=None
        nombres=request.form['nombresPersona']
        apellidos=request.form['apellidosPersona']
        tipoDocumento=request.form['tipoDocumentoPersona']
        documento=request.form['documentoPersona']
        correo=request.form['correoPersona']
        telefono=request.form['telefonoPersona']
        cur=con.cursor()
        cur.execute('update persona set nombres=?,apellidos=?,tipoIdentificacion=?,identificacion=?,telefono=?,email=? where idPersona=?',(nombres,apellidos,tipoDocumento,documento,telefono,correo,idPersona))
        con.commit()
        return redirect(url_for('Estudiante'))

    con=sql.connect('BaseNotas.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from persona where idPersona=?',(idPersona))
    data=cur.fetchone()
    return render_template('PersonaActualizar.html',datas=data)

    


@app.route('/deletePersona/<string:idPersona>',methods=['GET'])
def deletePersona(idPersona):
    con=sql.connect('BaseNotas.db')
    cur=con.cursor()
    cur.execute('update persona set estado="Inactivo" where idPersona=?',(idPersona))
    con.commit()
    flash('Usuario Eliminado','warning')
    return redirect(url_for('Estudiante'))



"---------------docente-----------------------"
@app.route('/Docente')
def Docente():
    con=sql.connect('BaseNotas.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from persona where estado="Activo" and idRol=2')
    data=cur.fetchall()
    return render_template('Docentes.html')

@app.route('/addDocente',methods=['GET','POST'])
def addDocente():
    if request.method=='POST':
        nombres=request.form['nombresPersona']
        apellidos=request.form['apellidosPersona']
        tipoDocumento=request.form['tipoDocumentoPersona']
        documento=request.form['identificacionPersona']
        correo=request.form['correoPersona']
        telefono=request.form['telefonoPersona']
        idRol=request.form['rolPersona']
        fechaRegistro= datetime.now()
        fechaActualizacion= datetime.now()
        estado='Activo'
        con=sql.connect('BaseNotas.db')
        cur=con.cursor()
        cur.execute('insert into persona (nombres,apellidos,tipoIdentificacion,identificacion,telefono,email,fechaRegistro,fechaActualizacion,idRol,estado) values (?,?,?,?,?,?,?,?,?,?)',(nombres,apellidos,tipoDocumento,documento,telefono,correo,fechaRegistro,fechaActualizacion,idRol,estado))
        con.commit()
        flash('Usuario Guardado','success')
        return redirect(url_for('Docente'))
    return render_template('Docente.html')

@app.route('/editDocente/<string:idPersona>',methods=['GET','POST'])
def editDocente(idPersona):
    if request.method == 'POST':
        
        con=sql.connect('BaseNotas.db')
        con.row_factory=sql.Row
        error=None
        nombres=request.form['nombresPersona']
        apellidos=request.form['apellidosPersona']
        tipoDocumento=request.form['tipoDocumentoPersona']
        documento=request.form['documentoPersona']
        correo=request.form['correoPersona']
        telefono=request.form['telefonoPersona']
        cur=con.cursor()
        cur.execute('update persona set nombres=?,apellidos=?,tipoIdentificacion=?,identificacion=?,telefono=?,email=? where idPersona=?',(nombres,apellidos,tipoDocumento,documento,telefono,correo,idPersona))
        con.commit()
        return redirect(url_for('Docente'))

    con=sql.connect('BaseNotas.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from persona where idPersona=?',(idPersona))
    data=cur.fetchone()
    return render_template('DocenteActualizar.html',datas=data)

    


@app.route('/deleteDocente/<string:idPersona>',methods=['GET'])
def deleteDocente(idPersona):
    con=sql.connect('BaseNotas.db')
    cur=con.cursor()
    cur.execute('update persona set estado="Inactivo" where idPersona=?',(idPersona))
    con.commit()
    flash('Usuario Eliminado','warning')
    return redirect(url_for('Docente'))

@app.route('/consultaDocente',methods=['GET','POST'])
def consultaDocente():      
    if request.method == 'POST':
        documentoFiltro=request.form['documentoFiltro']
        nombres=request.form['nombresFiltro']
        con=sql.connect('BaseNotas.db')
        con.row_factory=sql.Row
        cur=con.cursor()
        if documentoFiltro !='' or nombres!='':
            cur.execute('select * from persona WHERE identificacion=? or nombres=? and estado="Activo" and idRol=2',(documentoFiltro,nombres) )
           
        else:
            cur.execute('select * from persona where estado="Activo" and idRol=2') 
           
        data=cur.fetchall()
    return render_template('Docentes.html',datas=data)



@app.route('/Materias')
def Materias():
      return render_template('Materia.html')


@app.route('/Actividades')
def Actividades():
      return render_template('Actividades.html')







if __name__=='__main__':
    app.run(debug=True)