# Ruby - Básicos

estilo = "Rock"
duracao = "3"
puts("Estilo: " + estilo + "\nDuração: " + duracao + " minutos")

# Variáveis

inteiro = 1
float = 1.2
booleano = true
nulo = nil

array = [0,1,2,3,4,5,6,7,8,9]
puts array[0]
puts array[-1]
puts array[0, 3]
puts array[0..3]
puts array[0...3]
puts array.length()
puts array.include? 1
puts array.reverse()
puts array.sort()
puts array.uniq()
puts array.push(10)
puts array.pop()
puts array.shift()
puts array.unshift(0)
puts array.delete_at(0)
puts array.delete(1)
puts array.join(" ")

hash = {
    "primeira" => 1,
    "segunda" => 2,
    "terceira" => 3,
    "Exemplo" => "Teste",
    :Forma_nova => "funciona",
    10 => "Dez"
}
puts hash["Exemplo"]
puts hash[:Forma_nova]
puts hash[10]

# Strings

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


# Matemática e Números

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
puts("Cortando fora o decimal = " + num3.floor().to_s)


puts("Entre qualquer coisa:")
abc = gets.chomp()
puts("Você digitou: " + abc)

def printar_hello_world
    puts "Hello World"
end

printar_hello_world

def funcao_com_parametro(nome)
    puts("Olá " + nome)
end

funcao_com_parametro("João")

def funcao_com_parametro_default(nome = "Fulano")
    puts("Olá " + nome)
end

funcao_com_parametro_default

def funcao_com_return(num)
    return num * 2
end

numero = funcao_com_return(10)
puts(numero)

passaro = true
aviao = true
if passaro
    puts("É um pássaro")
elsif aviao
    puts("É um avião")
else
    puts("É o Superman")
end

negacao = false
if !negacao
    puts("Não é negação")
end
