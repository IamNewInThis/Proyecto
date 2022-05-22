 /*-----------------------CARRUCEL------------------------*/ 
let imagenBtn = document.querySelectorAll('.vid-btn');

imagenBtn.forEach(btn=>{
    btn.addEventListener('click', ()=>{
        document.querySelector('.controles .active').classList.remove('active');
        btn.classList.add('active');
        let src = btn.getAttribute('data-src');
        document.querySelector('#imagen-slider').src = src;
    });
});

/*-----------------------USER ICON------------------------*/ 
let user = document.querySelector('.user-icon');

document.querySelector('#user-btn').onclick=() =>{
    user.classList.add('active');
}

document.querySelector('#cerrar').onclick=() =>{
    user.classList.remove('active');
}

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