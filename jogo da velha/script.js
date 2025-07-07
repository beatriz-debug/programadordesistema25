var jogador = "x"

function jogar(celula) {

    //compara se a celula esta vazia para se escrever
    if(celula.innerHTML == "") {

        //escreva a letra na celula
        celula.innerHTML = jogador;

        //alterna a variavel jogador para a proxima jogada
        if(jogador == "x"){
            jogador = "o";
         }else{
            jogador = "x";
         }
    }

}