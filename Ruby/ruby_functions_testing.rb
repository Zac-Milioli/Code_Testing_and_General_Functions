# Ruby - Básicos
=begin
FEITO POR ZAC MILIOLI
ESTUDANDO RUBY BÁSICO
=end

estilo = "Rock"
duracao = "3"
puts("Estilo: #{estilo}\nDuração: #{duracao} minutos")

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

frase6 = "Fazendo um split"
puts(frase6.split(" "))

frase7 = "substituições cachorro"
puts(frase7.gsub('cachorro', 'bacanas'))


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

def match_case(dia)
    case day
    when "Segunda"
        puts("Dia de trabalho")
    when "Sábado"
        puts("Dia de descanso")
    else
        puts("Dia de qualquer coisa")
    end
    return "Fim"
end

index = 1
while index <= 10
    puts index
    index += 1
end

frutas = ["banana", "maçã", "morango", "abacaxi", "abacate"]
for i in frutas
    print i + ' '
end
puts

frutas.each do |i|
    print i + ' '
end
puts

6.times do |i|
    print i
end
puts

File.open("texto.txt", "r") do |file|
    for line in file.readlines()
        puts line
    end
    file.close()
end

File.open("texto.txt", "a") do |file|
    file.write("\nAdicionando linha nova")
    file.close()
end

begin
    num = 10/0
rescue ZeroDivisionError => e
    puts e
end

# Objetos e Módulos

class Feiticeiro
    attr_accessor :nome, :elemento, :poder
    def initialize(nome, elemento, poder)
        @nome = nome
        @elemento = elemento
        @poder = poder
        puts "O feiticeiro "+ @nome +" de " + @elemento + " se ergue com " + @poder.to_s + " de poder!"
    end

    def magia
        puts "Magia de " + @elemento + " foi lançada por " + @nome + "!"
    end
end

gargamel = Feiticeiro.new(nome="Gargamel", elemento="Pedra", poder=500)
gargamel.magia

class Familiar < Feiticeiro
    def initialize(pet_name, pet_type)
        @pet_name = pet_name
        @pet_type = pet_type
        puts "Encontra-se "+ @pet_name + ", um familiar do tipo " + @pet_type
    end
end

pet = Familiar.new(pet_name='Bobby', pet_type="Cão das neves")

module Various
    def hello_world_salted(salt)
        puts "hello world #{salt}!"
    end
    def greet(name)
        puts "Pleasured to meet you, #{name}"
    end
end

include Various
Various.hello_world_salted("Marcelo")
Various.greet("Lohaine")

# Usando a função system
system("echo Hello World!")

# Usando crases
`echo Hello World!`