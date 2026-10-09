from utils.formatting import print_tasks


def test_print_tasks(capsys):
    print_tasks([{"title": "Buy milk", "done": True}])
    assert "[x] Buy milk" in capsys.readouterr().out
