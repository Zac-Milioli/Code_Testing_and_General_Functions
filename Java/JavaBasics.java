class JavaBasics{
    static int var_global = 25;
    public static void main(String[] args){
        System.out.println("Hello world");
        int num = 10;
        System.out.printf("O número local é %d\n", num);
        System.out.printf("O número global é %d\n", var_global);
    }
}

// Solicitado ao Copilot para estudos
class VariableTypes {
    // Primitive types
    byte byteVariable; // 8-bit signed integer (-128 to 127)
    short shortVariable; // 16-bit signed integer (-32,768 to 32,767)
    int intVariable; // 32-bit signed integer (-2,147,483,648 to 2,147,483,647)
    long longVariable; // 64-bit signed integer (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
    float floatVariable; // 32-bit floating point (approximately ±3.40282347E+38F)
    double doubleVariable; // 64-bit floating point (approximately ±1.79769313486231570E+308)
    char charVariable; // 16-bit Unicode character (0 to 65,535)
    boolean booleanVariable; // true or false

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
        variableTypes.charVariable = 'A';
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