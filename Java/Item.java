public class Item{
    // attr accessor
    public String name;
    public String description;

    // __init__
    Item(String name, String description){
        this.name = name;
        this.description = description;
    }

    // Método de conversão de ponto de memória para string. Exibição. __str__
    public String toString(){
        return String.format("Item: %s. Descrição: %s", this.name, this.description);
    }
}