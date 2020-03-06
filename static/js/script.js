
function trocaEstilo(){
	  document.getElementById("title").className = "caixaTextoOnClick";
	  document.getElementById("btnPesquisa").setAttribute("style", "color: black;");
    btnPesquisa.setAttribute('onclick', 'voltaEstilo()')
}
function voltaEstilo(){
    document.getElementById("title").className = "caixaTexto";
    document.getElementById("btnPesquisa").setAttribute("style", "color: gray;");
    btnPesquisa.setAttribute('onclick', 'trocaEstilo()')
}
$('.carousel-item').first().addClass('active');
$('.indicadores').first().addClass('active');


var txtTitulo = 'Portfólio';
var txtT2 = 'Depoimentos';
var txt1 = document.getElementById("titulo");
var txt2 = document.getElementById("t2");
var speed = 100;
var cont = 0;
var cont2 = 0;

function typeWriter() {
    if(cont < txtTitulo.length){
        txt1.innerHTML +=  txtTitulo.charAt(cont);
        cont++;
        setTimeout(typeWriter, speed);
    }else{
        cont = 0;
    }
}
function typeWriter2() {
    if(cont2 < txtT2.length){
        txt2.innerHTML +=  txtT2.charAt(cont2);
        cont2++;
        setTimeout(typeWriter2, speed);
    }else{
        cont2 = 0;
    }
}                 

function myFunction() {
  	var endtela  = $(window).height()+$(window).scrollTop();
  	var initportifolio = $('.portfolio').offset().top;
  	var endportifolio  = $('.portfolio').offset().top+($('.portfolio').height()/2);
  	var initdepoimentos = $('.depoimentos').offset().top;

  	if (endtela > endportifolio) {
    	$('.fotos_portfolio').addClass('mostra_portifolio');
    	$('.fotos_portfolio').removeClass('esconde_portifolio');
  	} 
    if ($(window).scrollTop() < 50) {
      $('.logo').css('width','300px');
    }
  	if (endtela > initportifolio && $("#titulo").text() == ' ' ) {
    	typeWriter();
    }
    if (endtela > initdepoimentos && $("#t2").text() == ' ' ) {
    	typeWriter2();
    }
}
myFunction();

window.onscroll = function(){$('.logo').css('width','150px');myFunction();}
