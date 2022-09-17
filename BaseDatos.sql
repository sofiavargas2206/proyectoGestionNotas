create table rol (
idRol int primary key , 
rol varchar(50) not null,
fechaRegistro sysdate,
fecha actualizacion date
);


create table persona (
idPersona int primary key ,
nombres varchar(50) not  null,
apellidos varchar(50) not null,
tipoIdentificacion varchar(10) not null,
identificacion varchar(100) unique not null,
telefono varchar(20)  null,
email varchar(70) not null,
fechaRegistro sysdate not null,
fechaActualizacion date not null,
idRol int ,
foreign key (idRol) references rol(idRol)
 );