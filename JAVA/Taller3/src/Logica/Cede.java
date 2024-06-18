package Logica;

import java.util.ArrayList;
import java.util.List;

public class Cede {
	String nombre;
	int cantidadSoldados;
	String[] fuerzasArmadas;
	List<Soldado> soldados;

	public Cede(String nombre, int cantidadSoldados, String[] fuerzasArmadas) {
		this.nombre = nombre;
		this.cantidadSoldados = cantidadSoldados;
		this.fuerzasArmadas = fuerzasArmadas;
		soldados= new ArrayList<Soldado>();
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getCantidadSoldados() {
		return cantidadSoldados;
	}

	public List<Soldado> getSoldados() {
		return soldados;
	}

	public void setSoldados(List<Soldado> soldados) {
		this.soldados = soldados;
	}

	public void setCantidadSoldados(int cantidadSoldados) {
		this.cantidadSoldados = cantidadSoldados;
	}

	public String[] getFuerzasArmadas() {
		return fuerzasArmadas;
	}

	public void setFuerzasArmadas(String[] fuerzasArmadas) {
		this.fuerzasArmadas = fuerzasArmadas;
	}
	

}
