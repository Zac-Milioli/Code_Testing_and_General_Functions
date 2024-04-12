// Importando a função de input
import java.util.Scanner;

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
        System.out.println(opt1 && opt2);
        System.out.println(opt1 || opt2);
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

        scanner.close();
    }
}

// Solicitado ao Copilot para fins de estudo e documentação
class VariableTypes {
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