from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_main():
    payload = {
				"from_msg": "teste@gmail.com",
				"to_msg": [
					"lucaslimadecanto@gmail.com"
				],
				"subject": "Teste",
				"body": "Conteudo"
			}
    response = client.post(
        url="/api/send_email/",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    assert response.json() == {'msg': 'Message Sent Successfully!'}