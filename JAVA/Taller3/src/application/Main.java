package application;

import java.io.FileNotFoundException;
import java.util.List;

import Logica.Actividad;
import Logica.ActividadComponent;
import Logica.ColorDecorator;
import Logica.Marino;
import Logica.SistemaImp;
import Logica.Soldado;
import Logica.TxtManager;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;

public class Main extends Application {
	@Override
	public void start(Stage primaryStage) throws FileNotFoundException {

		try {
			Parent root = FXMLLoader.load(getClass().getResource("Menu2.fxml"));
			Scene scene = new Scene(root, 500, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	public static void main(String[] args) throws FileNotFoundException {
		
		SistemaImp.getInstance().leerArchivos();
		//lector.leerSoldados();
		 
		launch(args);

	}
}
