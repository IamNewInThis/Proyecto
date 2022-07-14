/*-----------------------CARRUCEL------------------------*/
let imagenBtn = document.querySelectorAll('.vid-btn');

imagenBtn.forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelector('.controles .active').classList.remove('active');
        btn.classList.add('active');
        let src = btn.getAttribute('data-src');
        document.querySelector('#imagen-slider').src = src;
    });
});

/*-----------------------USER ICON------------------------*/
let user = document.querySelector('.user-icon');

document.querySelector('#user-btn').onclick = () => {
    user.classList.add('active');
}

document.querySelector('#cerrar').onclick = () => {
    user.classList.remove('active');
}

/*---------------------GENERAR ICON-----------------------*/
let dada = document.querySelector('.gen-div');

document.querySelector('#gen').onclick = () => {
    dada.classList.add('active');
}
document.querySelector('#cerrar-popup').onclick = () => {
    dada.classList.remove('active');
}

/*-------------------VALIDACIÓN RUT y mensajes de error-------------------------*/
$(document).ready(function () {
    var validador = 0;
    var mensaje = "";
    console.log("probando equisde")
    $("#alerta").hide();
    document.getElementById('formularioregistro').addEventListener('submit', (e) => {
        e.preventDefault();
        var nombre = document.getElementById('id_nomb').value;
        var apellido = document.getElementById('id_ape').value;
        var direccion = document.getElementById('id_direc').value;
        var numtel = document.getElementById('id_num').value;
        var email = document.getElementById('id_email').value;
        var password = document.getElementById('id_pass').value;
        var fechnac = document.getElementById('id_date').value;
        var rut = document.getElementById('id_rut').value;
        if (nombre.length<3){
            alert('El nombre es demasiado corto');
            return;
        }
        if (numtel.length<9){
            alert('El número debe ser de 9 dígitos')
            return;
        }
        if (numtel.length>9){
            alert('El número debe ser de 9 dígitos')
            return;
        }
        if (password.length<5){
            alert('la contraseña debe ser de 5 caracteres o más')
            return;        
        }
        if (validador==2){
            alert('el rut ingresado no es válido')
            return;
        }
         
        $( "#formularioregistro" ).submit();
    })

    $("#id_nomb").focusout(function () {
        if ($("#id_nomb").val().length == 0) {
            //mostrar alerta
            mensaje = "Debe ingresar nombre";
            $("#alerta").html(mensaje);
            $("#alerta").show();
        } else {
            $("#alerta").hide();
        }
    });

    $("#id_ape").focusout(function () {
        if ($("#id_ape").val().length == 0) {
            //mostrar alerta
            mensaje = "Debe ingresar un apellido";
            $("#alerta").html(mensaje);
            $("#alerta").show();
        } else {
            $("#alerta").hide();
        }
    });

    $("#id_email").focusout(function () {
        if ($("#id_email").val().length == 0) {
            //mostrar alerta
            mensaje = "Debe ingresar Email";
            $("#alerta").html(mensaje);
            $("#alerta").show();
        } else {
            $("#alerta").hide();
        }
    });

    $("#id_pass").focusout(function () {
        if ($("#id_pass").val().length == 0) {
            //mostrar alerta
            mensaje = "Debe ingresar Contraseña";
            $("#alerta").html(mensaje);
            $("#alerta").show();
        } else {
            $("#alerta").hide();
        }
    });

    $("#id_direc").focusout(function () {
        if ($("#id_direc").val().length == 0) {
            //mostrar alerta
            mensaje = "Debe ingresar Dirección";
            $("#alerta").html(mensaje);
            $("#alerta").show();
        } else {
            $("#alerta").hide();
        }
    });

    $(function () {
        //$("#id_rut").focusout(function () {

       // });
        $("#id_rut").rut().on('rutValido', function (e, rut, dv) {
            alert("El rut " + rut + "-" + dv + " es correcto");
        }, { minimumLength: 7 });

        $("input#id_rut").rut();
        $("#id_rut").focusout(function () {
            if ($("#id_rut").val().length == 0) {
                //mostrar alerta
                mensaje = "Debe ingresar un rut";
                $("#alerta").html(mensaje);
                $("#alerta").show();
                console.log("ALERTA DE QUE NO HAY RUT")
            } else {
                $("#alerta").hide();
            }

            let rutvalor = document.getElementById("id_rut").value;
            console.log(rutvalor);
            let dvp = rutvalor[rutvalor.length - 1];
            rutvalor = rutvalor.replaceAll(".", "");
            rutvalor = rutvalor.replaceAll("-", "");
            rutvalor = rutvalor.substring(0, rutvalor.length - 1)
            console.log(rutvalor);
            let lista = [3, 2, 7, 6, 5, 4, 3, 2];
            let resultado = 0
            for (let i = 0; i < rutvalor.length; i++) {
                resultado += rutvalor[i] * lista[i];
            }
            resultado = resultado % 11
            let dv = 11 - resultado
            if (dv==11){
                dv=0
            } else if (dv==10){
                dv='k'
            }
            if (dv != dvp && $("#id_rut").val().length >0) {
                mensaje = "el rut es inválido"
                $("#alerta").html(mensaje);
                $("#alerta").show();
                validador = 2;
                console.log("ALERTA RUT INVALIDO")
            } else if (dv==dvp) {
                $("#alerta").hide();
                validador = 1;
            }

        });
    })

});

/*-----------------------VALIDAR TARJETA------------------------*/
const 
    tarjeta = document.querySelector("#nro_tarjeta"),
    btnAbrirFormulario = document.querySelector("#btn"),
    formulario = document.querySelector("#formulario_tarjeta");
    
//VALIDAR TARJETA
formulario.nro_tarjeta.addEventListener('keyup', (e)=>{
    let valorInput = e.target.value;

    formulario.nro_tarjeta.value = valorInput
	// Eliminamos espacios en blanco
	.replace(/\s/g, '')
	// Eliminar las letras
	.replace(/\D/g, '')
	// Ponemos espacio cada cuatro numeros
	.replace(/([0-9]{4})/g, '$1 ')
	// Elimina el ultimo espaciado
	.trim();

});

//VALIDAR NOMBRE
formulario.nombre.addEventListener('keyup', (e) => {
	debugger;
	let valorInput = e.target.value;
	formulario.nombre.value = valorInput.replace(/[0-9]/g, '');
});

// * Select del mes generado dinamicamente.
for(let i = 1; i <= 12; i++){
	let opcion = document.createElement('option');
	opcion.value = i;
	opcion.innerText = i;
	formulario.mes.appendChild(opcion);
}

// * Select del año generado dinamicamente.
const yearActual = new Date().getFullYear();
for(let i = yearActual; i <= yearActual + 8; i++){
	let opcion = document.createElement('option');
	opcion.value = i;
	opcion.innerText = i;
	formulario.año.appendChild(opcion);
}

// VALIDAR CVV
formulario.cvv.addEventListener('keyup', () => {
	
	formulario.cvv.value = formulario.cvv.value
	// Eliminar los espacios
	.replace(/\s/g, '')
	// Eliminar las letras
	.replace(/\D/g, '');
});