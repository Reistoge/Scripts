package Logica;

public class Soldado {
	String nombre,rut,contraseña,cede,tipo;

	public Soldado(String nombre, String rut, String contraseña, String cede, String tipo) {
		this.nombre = nombre;
		this.rut = rut;
		this.contraseña = contraseña;
		this.cede = cede;
		this.tipo = tipo;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getRut() {
		return rut;
	}

	public void setRut(String rut) {
		this.rut = rut;
	}

	public String getContraseña() {
		return contraseña;
	}

	public void setContraseña(String contraseña) {
		this.contraseña = contraseña;
	}

	public String getCede() {
		return cede;
	}

	public void setCede(String cede) {
		this.cede = cede;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	
	
	
	
}
