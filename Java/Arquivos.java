// Documentação sobre como criar, ler, modificar e excluir arquivos com java

import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class Arquivos {
    public static void main(String[] args) {
        try {
            // Criar um arquivo
            File file = new File("meuArquivo.txt");
            if (file.createNewFile()) {
                System.out.println("Arquivo criado: " + file.getName());
            } else {
                System.out.println("O arquivo já existe.");
            }

            // Ler o arquivo
            Scanner scanner = new Scanner(file);
            System.out.println("Conteúdo do arquivo:");
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                System.out.println(line);
            }
            scanner.close();

            // Modificar (escrever em) o arquivo
            FileWriter writer = new FileWriter("meuArquivo.txt");
            writer.write("Olá, Mundo!");
            writer.close();
            System.out.println("Escrita no arquivo concluída.");

            // Ler o arquivo novamente
            scanner = new Scanner(file);
            System.out.println("Conteúdo do arquivo após a modificação:");
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                System.out.println(line);
            }
            scanner.close();

            // Excluir o arquivo
            if (file.delete()) {
                System.out.println("Arquivo deletado: " + file.getName());
            } else {
                System.out.println("Falha ao deletar o arquivo.");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}