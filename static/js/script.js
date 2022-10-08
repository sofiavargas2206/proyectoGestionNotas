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

  
  
function Promedio(myArray){

  var i = 0, summ = 0, ArrayLen = myArray.length;
  while (i < ArrayLen) {
    summ = summ + myArray[i++];
    if(promedio >= 50.5){
      document.write("El promedio es "+promedio+" APROBADO");
    }else{
      document.write("El promedio es "+promedio+" DESAPROBADO");
    }
  }
    return summ / ArrayLen;
}
