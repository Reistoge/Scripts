package application;

 
import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import Logica.SistemaImp;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
 

public class LoginController extends MainController implements Initializable{
	
	
	@FXML
	private Button loginButton;
	@FXML
	private Button inscribirseButton;
	@FXML
	private Button sedesButton;
	@FXML
	private TextField userField;
	@FXML
	private TextField passField;
	@FXML
	private AnchorPane newSoldadoPane;
	@FXML
	private AnchorPane loginPane;
	
	String user;
	String pass;
	public void goToSedes(ActionEvent event) throws IOException{
		super.goToSedes(event);
	 
	}
	public void goToUsuario(ActionEvent event) throws IOException{
		// se verifica si el usario existe
		if(SistemaImp.getInstance().verifyUser(user,pass)) {
			
			super.goToUser(event);
			
		}
		
	}
	public void goToInscribirse(ActionEvent event) throws IOException{
		newSoldadoPane.setDisable(false);
		newSoldadoPane.setVisible(true);
		loginPane.setVisible(false);
		loginPane.setDisable(true);
	}
	
	
	@Override
	public void initialize(URL arg0, ResourceBundle arg1) {
		// TODO Auto-generated method stub
		
	 
	}
	
}
