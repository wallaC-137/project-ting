from pytest import raises
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    pq = PriorityQueue()

    pq.enqueue({"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 10})
    pq.enqueue({"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 3})
    pq.enqueue({"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 7})
    assert len(pq) == 3

    assert pq.dequeue() == {"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 3}
    assert pq.dequeue() == {"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 7}
    assert pq.dequeue() == {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 10,
    }
    assert len(pq) == 0

    with raises(IndexError):
        pq.search(7)
