alert("ola mundo");

//uma variavel guarda um valor temporariamente
// entrada de dados
var nome = "Bia"
var idade = "22"
var senha= "123"
 
//registrando alterações


//estrutura de condição
if (idade >= 18) {
    alert("pode votar!"+ nome);

} else{
    alert("vai embora daqui!"+nome);
}

if(nome == "Beatriz" && senha =="123"){
    alert("login concedido");
} else{
    alert("tente novamente!");
}
//laço de repetição
contador = 0;
while(contador < 1000) {
    contador = contador + 1;
    console.log(contador);
}


var celular = document.querySelector(".celular");      //icone de menu
var listamenu= document.querySelector(".menu ul");    //itens do menu

celular.addEventListener("click", function(){ 
    listamenu.classList.toggle("mostrarmenu");
});
//enviando alteração para github com visual studio code
//alterado no git