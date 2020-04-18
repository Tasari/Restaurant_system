from tables.worker import Worker
from tables.order import Order
from unittest.mock import MagicMock

def test_worker_creation():
    worker = Worker("toBias HayMond")
    assert worker.name == 'Tobias Haymond'
    assert worker.rank == 0
    assert worker.orders == []
    assert worker.work_hours == 0

def test_worker_promotion():
    worker = Worker("Foo Bar")
    worker.promotion()
    assert worker.rank == 1
    worker.promotion()
    assert worker.rank == 2
    worker.promotion(-1)
    assert worker.rank == 1

def test_worker_work_hours():
    worker = Worker("Eggs Ham")
    worker.add_work_hours(15)
    assert worker.work_hours == 15
    worker.add_work_hours(5)
    assert worker.work_hours == 20

def test_worker_finish_order():
    worker = Worker('Spam eggs')
    order = Order()
    order.add_product_to_order('Hamburger', 2)
    order.finish_order(MagicMock(), worker)
    assert order in worker.orders

def test_worker_orders_price():
    worker = Worker('Spam ham')
    order = Order()
    order.add_product_to_order('hamburger', 2)
    order.finish_order(MagicMock(), worker)
    order = Order()
    order.add_product_to_order('hamburger', 1)
    order.add_product_to_order('french fries', 1)
    order.finish_order(MagicMock(), worker)
    assert worker.orders_price_sum() == 5
    