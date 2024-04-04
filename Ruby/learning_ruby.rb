estilo = "Rock"
duracao = "3"
puts("Estilo: " + estilo + "\nDuração: " + duracao + " minutos")

inteiro = 1
float = 1.2
booleano = true
nulo = nil

frase = "   Hambuguer   "
puts(frase.strip())

frase1 = "TESTE"
puts(frase1.downcase())

frase2 = "teste"
puts(frase2.upcase())

frase3 = "Benzetacil"
puts(frase3.length())

frase4 = "Abacaxi"
puts(frase4.include? "apple")

frase5 = "Certa vez em Campo Grande"
puts(frase5[13, 24])
puts(frase5.index("Grande"))

puts 100 * 13
puts 2 ** 10
puts 100 + 13
puts 100 - 13
puts 100 % 13

num = 100
puts("Virando uma string = " + num.to_s)
num2 = -100
puts("ABS = " + num2.abs.to_s)
num3 = 3.14548
puts("Arredondando = " + num3.round().to_s)
puts("Arredondando pra cima = " + num3.ceil().to_s)