
 
let imagenBtn = document.querySelectorAll('.vid-btn');

imagenBtn.forEach(btn=>{
    btn.addEventListener('click', ()=>{
        document.querySelector('.controles .active').classList.remove('active');
        btn.classList.add('active');
        let src = btn.getAttribute('data-src');
        document.querySelector('#imagen-slider').src = src;
    });
});