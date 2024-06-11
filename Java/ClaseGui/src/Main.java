
import java.awt.BorderLayout;
import java.awt.Component;
 
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Scanner;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Main {
	public static void main(String[] args) {
		double time=0;
		Scanner scan = new Scanner(System.in);
		JFrame ventana = new JFrame("mi ventana");
		ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		ventana.setSize(300,400);
		ventana.getContentPane().add(createGUI());
		ventana.setVisible(true);
		
		
	}

	private static Component createGUI() {
		// TODO Auto-generated method stub
		JPanel mainPanel= new JPanel(new BorderLayout());
		
		JPanel botonera= new JPanel();
		
		botonera.setLayout(new BoxLayout(botonera, BoxLayout.LINE_AXIS));
		JPanel panelVacio= new JPanel();
		
		// elementos hacia abajo
		//panelVacio.setLayout(new BoxLayout(panelVacio, BoxLayout.PAGE_AXIS));
		JButton button1= new JButton("Button 1");
		JButton button3= crearBoton3(panelVacio);
		JButton button2= crearBoton2(panelVacio);
		botonera.add(button1);
		botonera.add(button2);
		botonera.add(button3);
		mainPanel.add(botonera,BorderLayout.NORTH);
		mainPanel.add(panelVacio,BorderLayout.CENTER);
		return mainPanel;
					
		
	}

	private static JButton crearBoton2(JPanel panelCentral) {
		JButton b = new JButton("Button 2");
		b.addActionListener(e->{
			System.out.println("hago click");
			panelCentral.add(new JLabel("Adios"));
			panelCentral.revalidate();
		});
		return b;
	}
	

	private static JButton crearBoton3(JPanel panelCentral) {
		JButton b = new JButton("Button3");
		b.addActionListener(e->{
			System.out.println("hago click");
			panelCentral.add(new JLabel("Hola"));
			panelCentral.revalidate();
		});
		return b;
	}

	private static JButton crearBoton3() {
	
		JButton b = new JButton("Button3");
		
		b.addActionListener( e ->{
			System.out.println("Hago click");
		});
		
		return b;
		
	}
	
}
class EscuchadorClick implements ActionListener{

	@Override
	public void actionPerformed(ActionEvent e) {
	 
		
		System.out.println("Hago click");
		
		
	}
	
}

