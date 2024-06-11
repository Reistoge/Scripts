package Logica;

public class SoldadoFactory {
	
	
	public SoldadoFactory() {
		
	}
	public Soldado crearSoldado(String[] datosSoldado) {
		
		String nombre=datosSoldado[0];
		String rut=datosSoldado[1];
		String contraseña=datosSoldado[2];
		String cede=datosSoldado[3];
		String tipo=datosSoldado[4];
		// los diferentes tipos de soldados se deben de construir de distinta manera.
		if(tipo.equalsIgnoreCase("fusilero")) {
			String arma=datosSoldado[5];
			String clase=datosSoldado[6];
			String pesoArma=datosSoldado[7];
			
			Fusilero f= new Fusilero(nombre,rut,contraseña,cede,tipo);
			f.setArma(pesoArma);
			f.setClase(clase);
			f.setPesoArma(pesoArma);
			
			return f;
			
			
		}
		else if(tipo.equalsIgnoreCase("marino")) {
			String tipoEmbarcacion=datosSoldado[5];
			String encargoEmbarcacion=datosSoldado[6];
			String puestoEmbarcacion=datosSoldado[7];
			 
			Marino m = new Marino(nombre,rut,contraseña,cede,tipo);
			
			m.setTipoEmbarcacion(tipoEmbarcacion);
			m.setTipoEncargo(encargoEmbarcacion);
			m.setPuestoEmbarcacion(puestoEmbarcacion);
			
			return m;
		}
		else if(tipo.equalsIgnoreCase("piloto")) {
			String lugarEspionaje=datosSoldado[5];
			String tipoNave=datosSoldado[6];
			String alturaDeVuelo=datosSoldado[7];
			Piloto p = new Piloto(nombre,rut,contraseña,cede,tipo);
			p.setLugarEspionaje(lugarEspionaje);
			p.setTipoNave(tipoNave);
			p.setAlturaVuelo(alturaDeVuelo);
			return p;
			
		}
		else if(tipo.equalsIgnoreCase("infante")) {
			String tipoDeRol=datosSoldado[5];
			String lugarQueVigila=datosSoldado[6];
			Infante inf= new Infante(nombre,rut,contraseña,cede,tipo);
			inf.setRol(tipoDeRol);
			inf.setLugarQueVigila(lugarQueVigila);
			return inf;
		}
		 
		return null;
		
	}
}
