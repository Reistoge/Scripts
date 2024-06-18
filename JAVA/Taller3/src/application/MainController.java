package application;

import java.io.IOException;

import javafx.application.Platform;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

public class MainController {

	@FXML
	private TextField userTextField;
	@FXML
	private Button homeButton;
	private Stage stage;
	private Parent root;
	private Scene scene;

	public void homeButton(ActionEvent event) throws IOException {
		Parent root = FXMLLoader.load(getClass().getResource("Menu2.fxml"));
		stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
		scene = new Scene(root, 500, 400);
		scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
		stage.setScene(scene);

	}

	public void goToUser(ActionEvent event, String tipoSoldado) throws IOException {
		Parent root = FXMLLoader.load(getClass().getResource(tipoSoldado + ".fxml"));
		stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
		scene = new Scene(root, 500, 400);
		scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
		stage.setScene(scene);

	}

	public void goToSedes(ActionEvent event) throws IOException {
		Parent root = FXMLLoader.load(getClass().getResource("Sedes.fxml"));
		stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
		scene = new Scene(root, 500, 400);
		scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
		stage.setScene(scene);

	}

	public void goToInscribirse(ActionEvent event) throws IOException {
		Parent root = FXMLLoader.load(getClass().getResource("Inscribirse.fxml"));
		stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
		scene = new Scene(root, 500, 400);
		scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
		stage.setScene(scene);

	}

}
