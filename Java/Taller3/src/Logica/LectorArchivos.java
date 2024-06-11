package Logica;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class LectorArchivos {
	// esta clase se encarga de leer linea por linea los archivos.
	
	SoldadoFactory soldadoFactory;
	public String leerSoldados() throws FileNotFoundException {
		
		Scanner scan= new Scanner(new File("Soldados.txt"));
		while(scan.hasNextLine()) {
			String[] partes= scan.nextLine().split(",");
			 soldadoFactory.crearSoldado(partes);

		}
		return null;
		
	}
	public String leerBrigadas() throws FileNotFoundException {
		Scanner scan = new Scanner(new File("brigadas.txt"));
		while(scan.hasNextLine()) {
			
		}
		return null;
	}
	public String leerActividades() throws FileNotFoundException {
		Scanner scan= new Scanner(new File("Soldados.txt"));
		while(scan.hasNextLine()) {
			
		}
		return null;
	}
	public String escrbirActividades() throws FileNotFoundException {
		Scanner scan= new Scanner(new File("Soldados.txt"));
		while(scan.hasNextLine()) {
			
		}
		return null;
	}
}
