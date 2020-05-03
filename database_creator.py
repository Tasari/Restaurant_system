import tables.stock
import tables.recipes
import tables.order_product
import tables.order
import tables.products
import tables.worker
from base_template import engine, Base, Session

Base.metadata.create_all(engine)
session = Session()
worker = tables.worker.Worker('Guest', 'guest', 'guest')
worker.promotion(50)
session.add(worker)
"""session.query(tables.stock.Stock).\
    update({tables.stock.Stock.quantity: 500})"""
session.commit()
session.close()