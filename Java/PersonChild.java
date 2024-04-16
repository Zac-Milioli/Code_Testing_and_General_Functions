// Trabalhando com herança
public class PersonChild extends Person{
    private String child;

    PersonChild(String name, String child){
        // o método super acessa e preenche os atributos da classe superior
        // podem ser definidos parâmetros "padrões", no exemplo a seguir foi a data
        // isso permite que o atributo possa não ser preenchido na criação do
        // objeto que herda de outros
        super(name, "2024-04-16");
        this.child = child;
    }

    public String getChild(){
        return this.child;
    }

    public String toString(){
        return String.format("%s de filho %s", this.name, this.child);
    }
}