package Logica;

import java.util.List;

public class SistemaImp implements ISistema {	
	
	private static SistemaImp instance;
	private int pass=123;
	private int user=432;
	List<Soldado> soldados;
	List<Cede> cedes; 
	private SistemaImp() {
	}
	public static SistemaImp getInstance() {
		
		if(instance==null) {
			instance= new SistemaImp();
		}
		return instance;
	}
	
	
	
	
	
	
	
	public int getPass() {
		return pass;
	}
	public void setPass(int pass) {
		this.pass = pass;
	}
	public int getUser() {
		return user;
	}
	public void setUser(int user) {
		this.user = user;
	}
	public boolean verifyUser(String user2, String pass2) {
		
		return false;
	}
	
	 
}
