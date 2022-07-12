$(document).ready(function(){
    let resultado=[]
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(mostrarPosicion);
        $('#solicitarclima').click(function(){
        getweather(resultado).then((clima)=>{
                console.log(clima)
                $('#tabla').append(`<tr><td>${clima.sys.country}</td><td>${clima.name}</td><td>${clima.main.temp_min}</td><td>${clima.main.temp_max}</td></tr>`)
            })
            
        })
    } else {
        alert("Tu navegador no soporta la geolocalización, actualiza tu navegador.");
    }

    function mostrarPosicion(posicion) {
    var latitud = posicion.coords.latitude;
    var longitud = posicion.coords.longitude;
    var precision = posicion.coords.accuracy;
    var fecha = new Date(posicion.timestamp);
    $('#posicion').append("Latitud: " + latitud + "");
    $('#posicion').append("Longitud:" + longitud + "");
    $('#posicion').append("Precisión: " + precision + " metros "); 
    $('#posicion').append("Fecha: " + fecha + "");  
    resultado.push(latitud);
    resultado.push(longitud);
}
    async function getweather(resultado){
        const response =  await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${resultado[0]}&lon=${resultado[1]}&appid=453a48cb8acfdae481c32b0282590ad8&units=metric`)
        const clima = await response.json()
        return clima

    }


    

});
