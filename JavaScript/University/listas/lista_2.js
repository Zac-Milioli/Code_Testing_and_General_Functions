// 1 Faça um Programa que tenha duas variáveis contendo números e imprima o maior deles.
function maior_de_2(num1, num2){
    if (num1 > num2){
        return num1
    } else if (num1 < num2){
        return num2
    } else {
        return "Eles são iguais"
    }
}

console.log(maior_de_2(1, 5))

// 2 Faça um Programa que dado um valor, mostre na tela se o valor é positivo ou negativo.
function positivo_negativo(){
    let valor = 2

    if (valor > 0){
        console.log("Positivo")
    } else if (valor < 0){
        console.log("Negativo")
    } else {
        console.log("Nem positivo nem negativo eu acho, o valor é zero. Se for saldo do banco acho que é mais positivo ser zero do que ser negativo, então de certo modo positivo")
    }
}

positivo_negativo()

/* 3 Faça um Programa que verifique se uma letra em uma variável é "F" ou "M". Conforme a
letra escrever: F - Feminino, M - Masculino, Sexo Inválido. */
function feminino_masculino_invalido(){
    let sexo = "Guaxinim"

    if (sexo === "F"){
        console.log("Feminino")
    } else if (sexo === "M"){
        console.log("Masculino")
    } else {
        console.log("Sexo Inválido")
    }
}

feminino_masculino_invalido()

// 4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
function vogal_consoante_nenhum(){
    let vogais = ["a", "e", "i", "o", "u"], consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    let letra = "$"

    if (vogais.includes(letra.toLowerCase())){
        console.log("É uma vogal")
    } else if (consoantes.includes(letra.toLowerCase())){
        console.log("É uma consoante")
    } else {
        console.log("Nem um nem outro")
    }
}

vogal_consoante_nenhum()

/* 5 Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez. */
function aprovado_reprovado(){
    let nota1 = 8, nota2 = 6
    let mean = (nota1+nota2)/2

    if (mean === 10){
        console.log("Aprovado com Distinção")
    } else if (mean >= 7){
        console.log("Aprovado")
    } else {
        console.log("Reprovado")
    }
}

aprovado_reprovado()

// 6 Faça um Programa que leia três números e mostre o maior deles.
function maior_de_3(num1, num2, num3){
    let maior_num1num2 = maior_de_2(num1, num2)
    let maior_de_todos = maior_de_2(maior_num1num2, num3)
    return maior_de_todos
}

console.log(maior_de_3(1,2,10))

// 7 Faça um Programa que leia três números e mostre o maior e o menor deles.
function menor_de_3(num1, num2, num3){
    if (num1 < num2 && num1 < num3) {
        return num1;
    } else if (num2 < num1 && num2 < num3) {
        return num2;
    } else {
        return num3;
    }
}

let n1 = 1, n2 = 2, n3 = 3
let maior = maior_de_3(n1,n2,n3), menor = menor_de_3(n1,n2,n3)

console.log(`Maior: ${maior}, Menor: ${menor}`)

/* 8 Faça um programa que pergunte o preço de três produtos e informe qual produto você
deve comprar, sabendo que a decisão é sempre pelo mais barato. */
let p1 = 1, p2 = 2, p3 = 3
let name1 = "p1", name2 = "p2", name3 = "p3"

function qual_comprar(produto1, produto2, produto3, nome1, nome2, nome3){
    let menor = menor_de_3(produto1, produto2, produto3)
    if (menor === produto1){return nome1}
    else if (menor === produto2){return nome2}
    else if (menor === produto3){return nome3}
    else{return "Erro"}
}

console.log(qual_comprar(p1,p2,p3,name1,name2,name3))

// 9 Faça um Programa que leia três números e mostre-os em ordem decrescente.
function decrescente(num1, num2, num3){
    let maior = maior_de_3(num1, num2, num3)
    let menor = menor_de_3(num1, num2, num3)
    
    if (maior === num1 && menor === num2){return [num1, num3, num2]}
    else if (maior === num1 && menor === num3){return [num1, num2, num3]}
    else if (maior === num2 && menor === num1){return [num2, num3, num1]}
    else if (maior === num2 && menor === num3){return [num2, num1, num3]}
    else if (maior === num3 && menor === num1){return [num3, num2, num1]}
    else if (maior === num3 && menor === num2){return [num3, num1, num2]}
    else{return "Erro"}
}

console.log(decrescente(2,1,3))