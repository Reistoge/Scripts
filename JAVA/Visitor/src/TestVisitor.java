import java.util.List;

public class TestVisitor {
	List<Circulo> circulos;
	List<Rectangulo> rectangulos;
	List<Triangulo> triangulos;
	public static void main(String[] args) {
		
	}
	
}
interface IVisitor{
	
	
	void visitar(Circulo circulo);

	void mostrarInfo(Figura r);

	void visitar(Rectangulo rectangulo);

	void visitar(Triangulo triangulo);
}
class LectorFiguras implements IVisitor{

	@Override
	public void visitar(Circulo circulo) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void visitar(Rectangulo rectangulo) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void visitar(Triangulo triangulo) {
		// TODO Auto-generated method stub
		
	}

	 

	@Override
	public void mostrarInfo(Figura r) {
		// TODO Auto-generated method stub
		
	}
	
}
class RenderizadorFiguras implements IVisitor{

	@Override
	public void visitar(Circulo circulo) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void visitar(Rectangulo rectangulo) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void visitar(Triangulo triangulo) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mostrarInfo(Figura r) {
		// TODO Auto-generated method stub
		
	}
	
}
abstract class Figura{
	abstract void accept(IVisitor r);
}
class Circulo extends Figura{

	@Override
	public void accept(IVisitor r) {
		r.visitar(this);
	}
	
}
class Rectangulo extends Figura{

	@Override
	public void accept(IVisitor r) {
		r.visitar(this);
	}
	
}
class Triangulo extends Figura{

	@Override
	public void accept(IVisitor r) {
		r.visitar(this);
	}
	
}
