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

@app.route('/addMateriaEstudiante',methods=['GET','POST'])
def addMateriaEstudiante():
    con=sql.connect('BaseNotas.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from materias where estado="Activo" and idRol=1')
    data=cur.fetchall()
    return render_template('Estudiante.html',datas=data)


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



"--------------Materias------------------"

@app.route('/Materias')
def Materias():
    con=sql.connect('BaseNotas.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from materia ')
    data=cur.fetchall()
    return render_template('Materia.html')

@app.route('/addMateria',methods=['GET','POST'])
def addMateria():
    if request.method=='POST':
        nombre=request.form['nombreMateria']
        fechaInicio=request.form['fechaInicio']
        fechaFin=request.form['fechaFin']
        fechaRegistro= datetime.now()
        fechaActualizacion= datetime.now()
        con=sql.connect('BaseNotas.db')
        cur=con.cursor()
        cur.execute('insert into materia (nombreMateria,fechaInicio,fechaFin,fechaRegistro,fechaActualizacion) values (?,?,?,?,?)',(nombre,fechaInicio,fechaFin,fechaRegistro,fechaActualizacion))
        con.commit()
        flash('Usuario Guardado','success')
        return redirect(url_for('Materias'))
    return render_template('Materia.html')

@app.route('/editMateria/<string:idMateria>',methods=['GET','POST'])
def editMateria(idMateria):
    if request.method == 'POST':
        
        con=sql.connect('BaseNotas.db')
        con.row_factory=sql.Row
        error=None
        nombre=request.form['nombreMateria']
        fechaInicio=request.form['fechaInicio']
        fechaFin=request.form['fechaFin']
        fechaActualizacion= datetime.now()
        cur=con.cursor()
        cur.execute('update materia set nombreMateria=?,fechaInicio=?,fechaFin=?, fechaActualizacion=? where idMateria=?',(nombre,fechaInicio,fechaFin,fechaActualizacion,idMateria))
        con.commit()
        return redirect(url_for('Materias'))

    con=sql.connect('BaseNotas.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from materia where idMateria=?',(idMateria))
    data=cur.fetchone()
    return render_template('MateriaActualizar.html',datas=data)

    


@app.route('/deleteMateria/<string:idMateria>',methods=['GET'])
def deleteMateria(idMateria):
    con=sql.connect('BaseNotas.db')
    cur=con.cursor()
    cur.execute('delete from materia where idMateria=?',(idMateria))
    con.commit()
    flash('Usuario Eliminado','warning')
    return redirect(url_for('Materias'))



@app.route('/consultaMateria',methods=['GET','POST'])
def consultaMateria():      
    if request.method == 'POST':
        IdenFiltro=request.form['idMateria']
        Materia=request.form['materiaFiltro']
        con=sql.connect('BaseNotas.db')
        con.row_factory=sql.Row
        cur=con.cursor()
        if IdenFiltro !='' or Materia!='':
            cur.execute('select * from materia WHERE idMateria=? or nombreMateria=?',(IdenFiltro,Materia) )
           
        else:
            cur.execute('select * from materia') 
        data=cur.fetchall()
    return render_template('Materia.html',datas=data)
    
    

@app.route('/Actividades')
def Actividades():
      return render_template('Actividades.html')







if __name__=='__main__':
    app.run(debug=True)