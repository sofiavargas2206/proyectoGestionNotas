function login(){
    var usuario=document.getElementById("usuario").value;
    var contraseñia = document.getElementById("contrasenia").value;
    
event.preventDefault();
  
  if(usuario!=null && contraseñia!=null){
    window.location.href="./Inicio.html";
}

}