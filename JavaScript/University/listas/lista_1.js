// 1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
console.log("Alo mundo")

/* 2 Faça um Programa que receba um número e então mostre a mensagem O número
informado foi [número]. */
let num = 5

console.log(`O número informado foi ${num}`)

// 3 Faça um Programa que faça a soma de dois números e imprima o resultado.
let num1 = 5, num2 = 10

console.log(num1+num2)

/* 4 Faça um Programa que tenha 4 variáveis representando as notas bimestrais e mostre a
média. */
let nota1 = 8, nota2 = 9, nota3 = 7.5, nota4 = 8.25
let mean = (nota1+nota2+nota3+nota4)/4

console.log(mean)

// 5 Faça um Programa que converta metros para centímetros.
let metros = 132

console.log(`A medida de ${metros} metros equivale a ${metros*100} centímetros`)

// 6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
let raio = 5

console.log(Math.PI*(raio**2))

/* 7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta
área para o usuário. */
let lateral = 10

console.log((lateral**2)*2)

/* 8 Faça um Programa que pegue o valor de uma variável que representa o valor por hora
trabalhada e o número de horas trabalhadas no mês. Calcule e mostre o total do salário no
referido mês. */
let valor_hora = 8, horas = 130

console.log(valor_hora*horas)

/* 9 Faça um Programa que converta a temperatura de graus Farenheit em graus Celsius e
imprima na tela.
C = (5 * (F-32) / 9). */
let graus_f = 77

console.log(5*(graus_f-32)/9)

/* 10 Faça um Programa que converta a temperatura de graus Celsius para graus Farenheit e
imprima na tela. */
let graus_c = 25

console.log((1.8*graus_c)+32)
