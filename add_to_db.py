from menu import Menu
from stock import Stock
from base_template import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

chicken_nugget = Stock('chicken_nugget', 0.15)
bun = Stock('bun', 0.20)
meat = Stock('meat', 0.30)
cheese = Stock('cheese', 0.10)
lettuce = Stock('lettuce', 0.05)
cola = Stock('cola', 0.1)

cheeseburger = Menu("Cheeseburger", 0.8)
burger_classic = Menu('Burger Classic', 1)
cola_drink = Menu('Cola', 0.3)
nuggets_x5 = Menu("5 Chicken Nuggets", 1)
nuggets_x10 = Menu("10 Chicken Nuggets", 1.90)

cheeseburger.recipe = [bun, cheese, meat]
burger_classic.recipe = [bun, cheese, meat, lettuce]
cola_drink.recipe = [cola]
nuggets_x5.recipe = [chicken_nugget]*5
nuggets_x10.recipe = [chicken_nugget]*10

session.add(chicken_nugget)
session.add(bun)
session.add(meat)
session.add(cheese)
session.add(lettuce)
session.add(cola)

session.add(cheeseburger)
session.add(burger_classic)
session.add(cola_drink)
session.add(nuggets_x5)
session.add(nuggets_x10)

session.commit()
session.close()