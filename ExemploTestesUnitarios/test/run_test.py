from run import divisao, informacoes

def test_divisao():
    assert divisao(50) == 25.0
    assert isinstance(divisao(50), float)

def test_informacoes():
    resp = informacoes()
    assert "name" in resp
    assert "height" not in resp
    assert "João Pedro" in resp["name"]