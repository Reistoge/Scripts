package Logica;

public class Infante extends Soldado{
	String rol,lugarQueVigila;
	public Infante(String nombre, String rut, String contraseña, String cede, String tipo) {
		super(nombre, rut, contraseña, cede, tipo);
		// TODO Auto-generated constructor stub
		rol="";
		lugarQueVigila="";
	}
	public String getRol() {
		return rol;
	}
	public void setRol(String rol) {
		this.rol = rol;
	}
	public String getLugarQueVigila() {
		return lugarQueVigila;
	}
	public void setLugarQueVigila(String lugarQueVigila) {
		this.lugarQueVigila = lugarQueVigila;
	}
	
}
