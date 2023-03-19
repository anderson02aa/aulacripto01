
function limpeza(){
	document.getElementById("saida").value = "";
	document.getElementById("entrada").value = "";
}
function ativarDivCripto(){
    document.getElementById("conteudo-principal").style.display = "none"
    document.getElementById("txt").style.display = "grid"
    document.getElementById("botoes").style.display = "block"
}
function ativarDivInfo(){
    document.getElementById("conteudo-principal").style.display = "block"
    document.getElementById("txt").style.display = "none"
    document.getElementById("botoes").style.display = "none"
}