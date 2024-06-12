package application;
import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
 
import javafx.application.Platform;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.TabPane;
import javafx.stage.Stage;
import javafx.scene.Node;
 
public class SceneController implements Initializable{
	
	
	@FXML
	private TabPane SedesTabPane;
	@FXML
	private Stage stage;
	private Scene scene;
	private Parent root;
	

	@Override
	public void initialize(URL arg0, ResourceBundle arg1) {
		// TODO Auto-generated method stub
		  
		 
		
	} 
	public void Menu(ActionEvent event) throws IOException{
		Parent root=FXMLLoader.load(getClass().getResource("Sign_up.fxml"));
		stage=(Stage) ((Node) event.getSource()).getScene().getWindow();
		scene= new Scene(root);
		stage.setScene(scene);
		stage.show();
		
	}
	
	
	
}
