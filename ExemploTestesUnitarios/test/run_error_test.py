from run import func_de_erro

def test_error():
    try:
        func_de_erro()
    except Exception as e:
        print(e)
        assert str(e) == "Algo deu errado"