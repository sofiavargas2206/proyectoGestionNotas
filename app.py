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
    cur.execute('select * from persona')
    data=cur.fetchall()
    return render_template('Estudiante.html',datas=data)


@app.route('/Docente')
def Docente():
      return render_template('Docentes.html')


@app.route('/Materias')
def Materias():
      return render_template('Materia.html')


@app.route('/Actividades')
def Actividades():
      return render_template('Actividades.html')





@app.route('/addPersona',methods=['GET','POST'])
def addPersona():
    if request.method=='POST':
        nombres=request.form['nombresPersona']
        apellidos=request.form['apellidosPersona']
        tipoDocumento=request.form['tipoDocumentoPersona']
        documento=request.form['identificacionPersona']
        correo=request.form['correoPersona']
        telefono=request.form['telefonoPersona']
        rol=request.form['rolPersona']
        fechaRegistro= datetime.now()
        fechaActualizacion= datetime.now()
        con=sql.connect('BaseNotas.db')
        cur=con.cursor()
        cur.execute('insert into persona (nombres,apellidos,tipoIdentificacion,identificacion,telefono,email,fechaRegistro,fechaActualizacion,idRol) values (?,?,?,?,?,?,?,?,?)',(nombres,apellidos,tipoDocumento,documento,telefono,correo,fechaRegistro,fechaActualizacion,rol))
        con.commit()
        flash('Usuario Guardado','success')
        return redirect(url_for('Estudiante'))
    return render_template('Estudiante.html')

@app.route('/editPersona/<string:idPersona>',methods=['GET','POST'])
def editPersona(idPersona):
    if request.method=='POST':
        nombres=request.form['nombresPersona']
        apellidos=request.form['apellidosPersona']
        tipoDocumento=request.form['tipoDocumentoPersona']
        documento=request.form['identificacionPersona']
        correo=request.form['correoPersona']
        telefono=request.form['telefonoPersona']
        rol=request.form['rolPersona']
        con=sql.connect('BaseNotas.db')
        cur=con.cursor()
        cur.execute('Update users set nombres=?,apellidos=?,tipoIdentificacion=?,identificacion=?,telefono=?,email=?,idRol=?',(nombres,apellidos,tipoDocumento,documento,telefono,correo,rol))
        con.commit()
        flash('Usuario Guardado','success')
        return redirect(url_for('Estudiante'))
    con=sql.connect('BaseNotas.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from users where idPersona=?',(idPersona))
    data=cur.fetchone()
    return render_template('Estudiante.html',datas=data)


@app.route('/deletePersona',methods=['GET','POST'])
def deletePersona():
    return render_template('Estudiante.html')




if __name__=='__main__':
    app.run(debug=True)