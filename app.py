from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql

app=Flask(__name__)
app.secret_key='admin123'

@app.route('/')
@app.route('/inicio')

def Estudiante():
    con=sql.connect('BaseNotas.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from persona')
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
        rol=request.form['rolPersona']

        con=sql.connect('BaseNotas.db')
        cur=con.cursor()
        cur.execute('insert into persona (nombres,apellidos,tipoIdentificacion,identificacion,telefono,email,idRol) values (?,?,?,?,?,?,?)',(nombres,apellidos,tipoDocumento,documento,telefono,correo,rol))
        con.commit()
        flash('Usuario Guardado','success')
        return redirect(url_for('Estudiante.html'))
    return render_template('Estudiante.html')




if __name__=='__main__':
    app.run(debug=True)