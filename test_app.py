from app import app

def test_home_status_code():
    # Cria um cliente de testes do Flask
    with app.test_client() as client:
        # Faz uma requisição GET na rota raiz "/"
        response = client.get("/")
        
        # Testa se o status code é 200
        assert response.status_code == 200