from pytest import raises
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()

    queue.enqueue({"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 10})
    queue.enqueue({"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 3})
    queue.enqueue({"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 7})
    assert len(queue) == 3

    assert queue.search(2) == {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 7,
    }

    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 3,
    }
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 10,
    }
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 7,
    }

    with raises(IndexError):
        queue.search(31)
