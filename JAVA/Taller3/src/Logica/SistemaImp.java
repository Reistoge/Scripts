package Logica;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;

public class SistemaImp implements ISistema {

	private static SistemaImp instance;

	ArrayList<Soldado> soldados;
	ArrayList<Cede> cedes;
	Soldado loggedSoldado;
	String[] colores = new String[3];

	private SistemaImp() {
		soldados = new ArrayList<Soldado>();
		cedes = new ArrayList<Cede>();
		loggedSoldado = null;
		colores[0] = "Alta";
		colores[1] = "Media";
		colores[2] = "Baja";

	}

	public static SistemaImp getInstance() {

		if (instance == null) {
			instance = new SistemaImp();
		}
		return instance;
	}

	public boolean verifyUser(String user2, String pass2) {
		// leer archivo .
//		try {
//			leerArchivos();
//
//		} catch (FileNotFoundException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
		System.out.println("intentando buscar usuario\nNombre: " + user2 + "\nContraseña: " + pass2);
		for (Soldado s : instance.soldados) {
			if (s.getNombre().equals(user2) && s.getContraseña().equals(pass2)) {
				// se verifica
				SistemaImp.instance.setLoggedSoldado(s);
				System.out.println("loggin con exito !");
				System.out.println(instance.getLoggedSoldado().toString());
				return true;
			}
		}
		System.out.println("contraseña o usuario incorrecto");
		return false;

	}

	public void leerArchivos() throws FileNotFoundException {
		//soldados= new ArrayList<Soldado>();
		//cedes = new ArrayList<Cede>();
		TxtManager txtManager = new TxtManager();
		// leemos primero las brigadas.
		txtManager.leerBrigadas();
		// leemos despues los soldados.
		txtManager.leerSoldados();
		// txtManager.leerActividades();
		

	}

	public ArrayList<Soldado> getSoldados() {
		return soldados;
	}

	public void setSoldados(ArrayList<Soldado> soldados) {
		this.soldados = soldados;
	}

	public List<Cede> getCedes() {
		return cedes;
	}

	public void setCedes(ArrayList<Cede> cedes) {
		this.cedes = cedes;
	}

	public Soldado getLoggedSoldado() {
		return loggedSoldado;
	}

	public void setLoggedSoldado(Soldado loggedSoldado) {
		this.loggedSoldado = loggedSoldado;
	}

	public static void setInstance(SistemaImp instance) {
		SistemaImp.instance = instance;
	}

	public String[] getActividadColores() {
		// TODO Auto-generated method stub
		return SistemaImp.instance.colores;
	}
	
	public void agregarActividad(ActividadComponent a) {
		loggedSoldado.actividades.add(a);
	}
	public void agregarSoldado(Soldado s) {
		
		// añadir una funcion la cual redirija a la cede del soldado.
		Cede c = getCede(s.getCede());
		if(c!=null) {
			// agregamos a la cede del soldado.
			c.soldados.add(s);
			 
		}
		//agregamos a los datos.
		soldados.add(s);
		
	}
	public Cede getCede(String lugar) {
		for(Cede c: cedes) {
			if(c.getNombre().equalsIgnoreCase(lugar)) {
				return c;
			}
		}
		return null;
	}
	
	
	public void setMarinosDeEmbarcacion(Marino marino) {
		ArrayList<Soldado> soldados = getInstance().soldados;
		ArrayList<Marino> marinos = new ArrayList<Marino>();
		for(Soldado s : soldados) {
			if( s instanceof Marino) {
				Marino m = (Marino) s;
				if(marino.getEmbarcacion().equalsIgnoreCase(m.getEmbarcacion()) && !m.equals(marino) ) {
					marino.getMarineros().add(m);
					
					
				}
				 
			}
		}	
		
	}
	public boolean promoverGrumete(String nombre, String rut, Marino user) {
		for(Marino m : user.getMarineros()) {
			if(m.getNombre().equalsIgnoreCase(nombre) && m.getRut().equalsIgnoreCase(rut)) {
				m.setPuestoEmbarcacion("Marinero");
				return true;
			}
		}
		return false;

		
		
	}
	public boolean descenderMarinero( String nombre, String rut, Marino user) {
		for(Marino m : user.getMarineros()) {
			if(m.getNombre().equalsIgnoreCase(nombre) && m.getRut().equalsIgnoreCase(rut)) {
				m.setPuestoEmbarcacion("Grumete");
				return true;
			}
		}
		return false;
		
	}
}
