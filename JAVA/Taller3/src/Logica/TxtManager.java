package Logica;

import java.io.File;
import java.io.FileNotFoundException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class TxtManager {
	// esta clase se encarga de leer linea por linea los archivos.

	public TxtManager() {

	}
	 
	public void leerSoldados() throws FileNotFoundException {
		SoldadoFactory soldadoFactory = new SoldadoFactory();
		int n = 0;
		Scanner scan = new Scanner(new File("Soldados.txt"));
		while (scan.hasNextLine()) {
			String[] partes = scan.nextLine().split(",");
			
			
			Soldado s=soldadoFactory.crearSoldado(partes);
			SistemaImp.getInstance().agregarSoldado(s);
			n++;
		}
		
		for(Soldado s: SistemaImp.getInstance().getSoldados()) {
			if(s instanceof Marino) {
				
				SistemaImp.getInstance().setMarinosDeEmbarcacion((Marino) s);
				
			}
			
		}
		
		
		if (n == SistemaImp.getInstance().getSoldados().size()) {

			System.out.println("se han cargado todos los soldados.");
		} else {
			System.out.println("no se han cargado todos los soldados");
		}

	}

	public String leerBrigadas() throws FileNotFoundException {
		Scanner scan = new Scanner(new File("brigadas.txt"));
		while (scan.hasNextLine()) {
				String[] lineaPartes= scan.nextLine().split(",");
				Cede c= new Cede(lineaPartes[0], Integer.parseInt(lineaPartes[1]), Arrays.copyOfRange(lineaPartes, 2, lineaPartes.length-1));
				SistemaImp.getInstance().getCedes().add(c);
		}
		System.out.println("Cedes leidas correctamente.");
		return null;
	}

	public String leerActividades() throws FileNotFoundException {
		Scanner scan = new Scanner(new File("Soldados.txt"));
		while (scan.hasNextLine()) {

		}
		return null;
	}

	public String escrbirActividades() throws FileNotFoundException {
		Scanner scan = new Scanner(new File("Soldados.txt"));
		while (scan.hasNextLine()) {

		}
		return null;
	}
}
