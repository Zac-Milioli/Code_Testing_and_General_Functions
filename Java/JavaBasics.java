// Importando a função de input
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.time.LocalDate;

class JavaBasics{
    static int var_global = 25;
    public static void main(String[] args){
        // println é usada para printar com uma nova linha ao final
        System.out.println("Hello world" + "!");
        int num = 10;
        // printf é usada para printar formatados com uma nova linha ao final
        System.out.printf("O número local é %d\n", num);
        System.out.printf("O número global é %d\n", var_global);
        // print é usando para printar itens sem uma nova linha ao final
        System.out.print("Exemplo linha 1 -- ");
        System.out.println("Exemplo linha 2");

        boolean opt1 = true, opt2 = false;
        // AND
        System.out.println(opt1 && opt2);
        // OR
        System.out.println(opt1 || opt2);
        // NOT
        System.out.println(!opt1);

        int soma1 = 0, subtrai1 = 10;
        // Operadores após a varável: valor é incrementado após uma iteração
        soma1++;
        subtrai1--;
        // Operadores antes da variável: valor é incrementado na mesma hora
        ++soma1;
        --subtrai1;
        System.out.println(soma1);
        System.out.println(subtrai1);

        // Cria uma string literal
        String frase1 = "Exemplo da primeira forma";
        String frase1_alt = "Exemplo da primeira forma";
        // Cria um novo objeto string, portanto, mesmo que existe dois objetos string com
        // o mesmo valor, eles não serão iguais
        String frase2 = new String("Exemplo da segunda forma");
        String frase2_alt = new String("Exemplo da segunda forma");

        System.out.println(frase1);
        System.out.println(frase2);

        System.out.println(frase1 == frase1_alt);
        System.out.println(frase2 == frase2_alt);
        // Porém, caso a comparação seja feita usando o método equals, apenas o valor literal é comparado
        System.out.println(frase2.equals(frase2_alt));
        // Inclusive ignorando letras maíusculas e minúsculas
        System.out.println(frase2.equalsIgnoreCase(frase2_alt));


        // Formatação de strings
        String myName = "Zac", myJob = "developer", myWorkplace = "LabEEE";
        int myAge = 22;

        // A formatação pode ser feita também diretamente dentro do "print", substituindo o println por printf
        // %s representa strings
        // %d representa inteiros
        // %f representa float
        // %c representa caracteres
        // %b representa booleanos
        // %n representa uma nova linha
        String formatada = String.format("Meu nome é %s, eu tenho %d anos de idade. Atualmente, eu trabalho como %s no %s", myName, myAge, myJob, myWorkplace); 
        System.out.println(formatada);

        // Alternativamente, existe a função StringBuilder ou StringBuffer
        StringBuilder sb = new StringBuilder();
        sb.append("Meu nome é ");
        sb.append(myName);
        sb.append(" e eu tenho ");
        sb.append(myAge);
        sb.append(" anos.");
        System.out.println(sb.toString());

        // Verificar se uma string é vazia ou não
        String vazia = "";
        System.out.println(vazia.isEmpty());
        // Retornar tamanho de string
        String tamanho = "123456789";
        System.out.println(tamanho.length());
        // Upercase e Lowercase
        String vira = "AbCdEfG";
        System.out.println(vira.toUpperCase());
        System.out.println(vira.toLowerCase());
        // Substituir um valor por outro
        String palavra = "Guarda-chuva";
        System.out.println(palavra.replace("chuva", "roupa"));
        // Verificar valores contidos
        System.out.println(palavra.contains("Guarda"));

        // Recebendo inputs do usuário
        Scanner scanner = new Scanner(System.in);

        System.out.print("\nDIGITE UMA STRING: ");
        // Recebendo string
        String valor_str_inserido = scanner.nextLine();
        System.out.println(valor_str_inserido);
        // Recebendo int
        System.out.print("\nDIGITE UM INT: ");
        int valor_int_inserido = scanner.nextInt();
        System.out.println(valor_int_inserido);
        // Existe um input diferente para cada tipo diferente de variável
        
        // Para cada método diferente de input, o <ENTER> fica registrado
        // no buffer deste método. Isso faz com que, caso seja feito mais
        // de uma vez o mesmo tipo de input (nextLine, nextInt, nextFloat...)
        // o valor <ENTER> seja verificado pelo objeto Scanner e automaticamente
        // toma o valor vazio como input. Por isso, é necessário limpar
        // o buffer a cada uso do método.
        // Para limpar o buffer, basta executar o método de input novamente
        // sem atribuí-lo a nenhuma variável.
        // Uma boa prática para prevenir confusões é utilizar sempre nextLine
        // para receber inputs, e convertê-los depois.
        scanner.nextLine();
        System.out.print("\nINSIRA UMA STRING PARA CONVERTER PARA INT: ");
        // As conversões são sempre feitas chamando o tipo de variável em
        // pascal case, seguido da função parse com o nome do tipo em camel case
        int int_convertido = Integer.parseInt(scanner.nextLine());
        System.out.println(int_convertido);

        System.out.println("\n".repeat(60));

        System.out.println("Calculadora");
        System.out.println("Digite dois valores");
        System.out.println("- ".repeat(45));

        System.out.print("- ");
        double num1 = scanner.nextDouble();
        scanner.nextLine();
        
        System.out.print("- ");
        double num2 = scanner.nextDouble();
        scanner.nextLine();
        
        System.out.println("\nDigite o operador");
        System.out.print("- ");
        String operator = scanner.nextLine();

        if (operator.equals("+")){
            System.out.printf("%f + %f = %f", num1, num2, num1+num2);
        } else if (operator.equals("-")){
            System.out.printf("%f - %f = %f", num1, num2, num1-num2);
        } else if (operator.equals("*") || operator.toLowerCase().equals("x")){
            System.out.printf("%f * %f = %f", num1, num2, num1*num2);
        } else if (operator.equals("/") || operator.equals("\\")){
            if (num2 != 0){
                System.out.printf("%f / %f = %f", num1, num2, num1/num2);
            } else {
                System.out.printf("DIVISÃO POR ZERO!!");
            }
        } else if (operator.equals("%")){
            System.out.printf("%f %% %f = %f", num1, num2, num1%num2);
        } else {
            System.out.printf("A operação %s não é suportada", operator);
        }

        System.out.println("\n".repeat(60));
        System.out.println("Digite as 3 primeiras letras de qualquer dia da semana");
        System.out.println("- ".repeat(45));
        String dia_semana = scanner.nextLine();

        switch(dia_semana.toLowerCase()){
            case "dom":
                System.out.printf("%s significa Domingo!", dia_semana);
                break;
            case "seg":
                System.out.printf("%s significa Segunda!", dia_semana);
                break;
            case "ter":
                System.out.printf("%s significa Terça!", dia_semana);
                break;
            case "qua":
                System.out.printf("%s significa Quarta!", dia_semana);
                break;
            case "qui":
                System.out.printf("%s significa Quinta!", dia_semana);
                break;
            case "sex":
                System.out.printf("%s significa Sexta!", dia_semana);
                break;
            case "sab":
                System.out.printf("%s significa Sábado!", dia_semana);
                break;
            default:
                System.out.printf("%s não é um dia da semana", dia_semana);    
        }
        scanner.close();
        System.out.println("\n".repeat(10));

        // Arrays
        String week[] = new String[7];
        String week2[] = {"Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"};

        week[0] = "Domingo";
        week[1] = "Segunda";
        week[2] = "Terça";
        week[3] = "Quarta";
        week[4] = "Quinta";
        week[5] = "Sexta";
        week[6] = "Sábado";

        System.out.println(week);
        System.out.println(week[2]);
        System.out.println(Arrays.toString(week));
        System.out.println(week2);
        System.out.println(week2[2]);
        System.out.println(Arrays.toString(week2));
        System.out.println(week2.length);

        // Pode ser adicionado slices no sort, fazendo Arrays.sort(lista, começo_index, fim_index) com o fim não incluso
        Arrays.sort(week);
        System.out.println(Arrays.toString(week));

        String busca = "Sábado";
        // Pode ser adicionado slices de busca no binarySearch, fazendo Arrays.binarySearch(lista, começo_idex, fim_index, valor_buscado) com o fim não incluso
        int buscarItem = Arrays.binarySearch(week2, busca);
        System.out.printf("Encontrou %s no index %d\n", busca, buscarItem);

        // Este método substitui todos os itens selecionados pelo parâmetro passado. Pode ser adicionado index de início e fim, com o fim não incluso
        Arrays.fill(week, "Zac");
        System.out.println(Arrays.toString(week));

        int[] nums = {1,2,3,4,5,6,7,8};
        int[] numsCopia = nums;
        System.out.println(Arrays.toString(nums));
        System.out.println(Arrays.toString(numsCopia));
        // Java lida com variáveis recebendo outras como valor apontando ambas para o mesmo espaço de memória,
        // portanto, modificações feitas em uma são aplicadas na outra
        // Uma cópia em um espaço de memória diferente pode ser feita da seguinte forma
        int[] numsCopiaDiferente = Arrays.copyOf(nums, nums.length);
        // Caso queira mudar o tamanho do Array sendo copiado, basta alterar o tamanho. Caso seja maior, incluirá 0 nos espaços não existentes
        // Se for menor, será feito slicing
        // Alternativamente, pode ser selecionado o range a ser usado fazendo Arrays.copyOfRange(lista, começo_index, fim_index) com o fim não incluso
        int[] numsCopiaRange = Arrays.copyOfRange(nums, 0, 5);
        Arrays.fill(nums, 0);
        System.out.println(Arrays.toString(nums));
        System.out.println(Arrays.toString(numsCopia));
        System.out.println(Arrays.toString(numsCopiaDiferente));
        System.out.println(Arrays.toString(numsCopiaRange));

        // LOOPS

        // Equivalente ao "for _ in lista:" do python
        for (int i : numsCopiaDiferente){
            System.out.println(i);
        }

        System.out.println("\n".repeat(10));
        for (int numero = 1; numero <= 10; numero++){
            System.out.println(numero);
        }

        int soma = 0;
        int stop = 50;
        while (soma <= stop){
            System.out.println(soma);
            soma++;
        }

        // Forma alternativa de usar while loop. A condição é verificada ao final do loop ao invés do início
        soma = 0;
        do{
            System.out.println(soma);
            soma++;
        } while(soma <= stop);

        // Criando um array lista
        // Todos os valores primitivos possuem uma versão class com funções extras
        ArrayList<Integer> numbersList = new ArrayList<Integer>();
        numbersList.add(1);
        numbersList.add(2);
        numbersList.add(1);
        numbersList.add(4);
        numbersList.add(6);
        numbersList.add(10);
        System.out.println(numbersList.toString());
        // O get usa o index para buscar
        System.out.println(numbersList.get(4));
        // O remove também usa o index
        numbersList.remove(3);
        System.out.println(numbersList.toString());
        // O index de valores diferentes pode ser buscado usando valueOf
        numbersList.remove(Integer.valueOf(1));
        System.out.println(numbersList.toString());
        // A lista pode ser limpa usando o método clear
        // numbersList.clear();
        // A função valueOf também pode ser usada para adicionar itens a um array list
        numbersList.set(1, Integer.valueOf(40));
        System.out.println(numbersList.toString());
        // Para ordenar listas é necessário usar alguma função do Comparator
        numbersList.sort(Comparator.naturalOrder());
        System.out.println(numbersList.toString());
        numbersList.sort(Comparator.reverseOrder());
        System.out.println(numbersList.toString());
        // Para retornar o tamanho
        System.out.println(numbersList.size());
        // Para verificar se há um valor específico na lista
        System.out.println(numbersList.contains(Integer.valueOf(40)));
        // Verificar se é vazio
        System.out.println(numbersList.isEmpty());
        
        // Loop para percorrer a lista
        numbersList.forEach(variavel_loop -> {
            System.out.println(variavel_loop);
        });
        
        // Exemplo de aplicação
        numbersList.forEach(valor_index -> {
            numbersList.set(numbersList.indexOf(valor_index), valor_index*2);
        });
        System.out.println(numbersList.toString());


        System.out.println("\n".repeat(10));

        // Dentro de hashmaps os pares precisam ter seus tipos indicados
        HashMap<String, Integer> estoque = new HashMap<String, Integer>();
        // O método put serve para incluir itens dentro de um hashmap
        estoque.put("Arroz", 21);
        estoque.put("Feijão", 18);
        estoque.put("Farinha", 20);
        estoque.put("Pão", 9);
        // Alternativamente, itens podem ser incluidos APENAS se ainda não existirem no HashMap usando putIfAbsent
        // Caso o item exista, a função é skipada
        estoque.putIfAbsent("Feijão", 10);
        estoque.putIfAbsent("Macarrão", 8);
        // O valor das chaves pode ser atualizado ou alterado utilizando o método replace
        estoque.replace("Arroz", 16);
        // O hashmap pode ser limpo usando o método clear
        // estoque.clear();

        // A remoção de itens pode ser feita com o método remove
        estoque.remove("Macarrão");

        System.out.println(estoque.toString());

        // Para buscar itens no hashmap pode ser usado o método get, retornando null caso o item não exista
        System.out.println(estoque.get("Pão"));
        // Alternativamente, pode ser usado o método getOrDefault para retornar um valor definido caso o item não exista
        System.out.println(estoque.getOrDefault("Chocolate", -1));
        // Para verificar a presença de alguma chave ou valor no hashmap podem ser usadas as funções contaisKey e containsValue
        System.out.println(estoque.containsKey("Arroz"));
        System.out.println(estoque.containsValue(Integer.valueOf(16)));
        // Pode verificar se o hashmap é vazio usando a função isEmpty
        System.out.println(estoque.isEmpty());
        // Loop que precorre o hashmap tal qual "for key, value in hashmap:"
        estoque.forEach((key, value) -> {
            System.out.println(key + " na quantidade " + value);
            estoque.replace(key, value+5);
        });
        System.out.println(estoque.toString());

        // Mexendo com objetos
        System.out.println("\n".repeat(10));
        Person pessoa1 = new Person("Test Buddy 1", "2024-04-16");
        System.out.printf("%s é o primeiro teste com orientação a objetos em java,\nfeito em %s, ou seja, %d dias atrás\n", pessoa1.name, pessoa1.getDate(), pessoa1.tempoPassado());
    
        Item chaveDeFenda = new Item("Chave de Fenda", "Uma ferramenta muito util");

        pessoa1.colocarNoInventario(chaveDeFenda);

        System.out.println("\nInventário:");
        System.out.println(pessoa1.inventory.toString());

        PersonChild pessoa2 = new PersonChild("Megaman", "Filho do Megaman");
        System.out.println(pessoa2);
    }
}


// Solicitado ao Copilot para fins de estudo e documentação
public class VariableTypes {
    // Primitive types

    // Integer
    byte byteVariable; // 8-bit signed integer (-128 to 127)
    short shortVariable; // 16-bit signed integer (-32,768 to 32,767)
    int intVariable; // 32-bit signed integer (-2,147,483,648 to 2,147,483,647)
    long longVariable; // 64-bit signed integer (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)

    // Decimals
    float floatVariable; // 32-bit floating point (approximately ±3.40282347E+38F)
    double doubleVariable; // 64-bit floating point (approximately ±1.79769313486231570E+308)

    // Bool
    boolean booleanVariable; // true or false
    
    // Characters
    char charVariable; // 16-bit Unicode character (0 to 65,535)

    // Reference types
    String stringVariable; // sequence of characters
    MyClass objectVariable; // reference to an object of MyClass

    public static void main(String[] args) {
        VariableTypes variableTypes = new VariableTypes();

        // Assign values to variables
        variableTypes.byteVariable = 10;
        variableTypes.shortVariable = 20;
        variableTypes.intVariable = 30;
        variableTypes.longVariable = 40L;
        variableTypes.floatVariable = 50.5f;
        variableTypes.doubleVariable = 60.6;
        variableTypes.charVariable = '\u00A9'; // Copyright Symbol
        variableTypes.booleanVariable = true;
        variableTypes.stringVariable = "Hello";
        variableTypes.objectVariable = new MyClass();

        // Print variable values
        System.out.println("byteVariable: " + variableTypes.byteVariable);
        System.out.println("shortVariable: " + variableTypes.shortVariable);
        System.out.println("intVariable: " + variableTypes.intVariable);
        System.out.println("longVariable: " + variableTypes.longVariable);
        System.out.println("floatVariable: " + variableTypes.floatVariable);
        System.out.println("doubleVariable: " + variableTypes.doubleVariable);
        System.out.println("charVariable: " + variableTypes.charVariable);
        System.out.println("booleanVariable: " + variableTypes.booleanVariable);
        System.out.println("stringVariable: " + variableTypes.stringVariable);
        System.out.println("objectVariable: " + variableTypes.objectVariable);
    }

    static class MyClass {
        // Class definition
    }
}