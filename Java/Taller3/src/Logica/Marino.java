package Logica;

public class Marino extends Soldado{
	String tipoEmbarcacion,tipoEncargo,puestoEmbarcacion;
	public Marino(String nombre, String rut, String contraseña, String cede, String tipo) {
		super(nombre, rut, contraseña, cede, tipo);
		// TODO Auto-generated constructor stub
	}
	public String getTipoEmbarcacion() {
		return tipoEmbarcacion;
	}
	public void setTipoEmbarcacion(String tipoEmbarcacion) {
		this.tipoEmbarcacion = tipoEmbarcacion;
	}
	public String getTipoEncargo() {
		return tipoEncargo;
	}
	public void setTipoEncargo(String tipoEncargo) {
		this.tipoEncargo = tipoEncargo;
	}
	public String getPuestoEmbarcacion() {
		return puestoEmbarcacion;
	}
	public void setPuestoEmbarcacion(String puestoEmbarcacion) {
		this.puestoEmbarcacion = puestoEmbarcacion;
	}

}
