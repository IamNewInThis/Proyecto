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
    var mensaje = "";
    console.log("probando equisde")
    $("#alerta").hide();

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
            mensaje = "Debe ingresar email";
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
            if (dv != dvp && $("#id_rut").val().length >0)  {
                mensaje = "el rut es inválido"
                $("#alerta").html(mensaje);
                $("#alerta").show();
                console.log("ALERTA RUT INVALIDO")
            } else if (dv==dvp) {
                $("#alerta").hide();
            }

        });
    })

});
