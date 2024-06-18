package Logica;

public class Actividad implements ActividadComponent {
	String nombre;
	String descripcion;

	public Actividad(String nombre, String descripcion) {
		this.nombre = nombre;
		this.descripcion = descripcion;
	}

	@Override
	public String getDatos() {
		// se necesitan los datos separados por coma.
		return this.nombre + "\t" + this.descripcion;

	}

}
