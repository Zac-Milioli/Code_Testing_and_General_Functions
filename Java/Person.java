import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

// this == self

public class Person{
    // attr accessor
    public String name;
    public ArrayList<Item> inventory = new ArrayList<Item>();
    // Atributo privado. Equivale ao _ e __ do python
    private LocalDate registerDate;

    // Construtor, init, inicializador
    Person(String name, String registerDate){
        this.name = name;
        this.registerDate = LocalDate.parse(registerDate);
    }

    // Métodos
    public void colocarNoInventario(Item item){
        this.inventory.add(item);
    }
    public void retirarDoInventario(Item item){
        this.inventory.remove(item);
    }
    public int tempoPassado(){
        int tempoPassado = Period.between(this.registerDate, LocalDate.now()).getDays();
        // Existem outros get para o LocalDate, tal como getYears, que retorna o tempo no formato pedido
        return tempoPassado;
    }
    public String getDate(){
        return this.registerDate.toString();
    }
}