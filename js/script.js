function login(){
    var usuario=document.getElementById("usuario").value;
    var contrasenia = document.getElementById("contrasenia").value;
    
    event.preventDefault();
   
  
  if(usuario!=null && contrasenia!=null){
    window.location.href="./Inicio.html";
        }

}
function myFunction() {
   
    //document.getElementById("modalContainer").style.display = none;
    document.getElementById('modalContainer').style.display='block';
  }
  function cerrarPop(){
    document.getElementById('modalContainer').style.display='none';
}
  