class Meal:
    def __init__(self):
        self.cost = 0.0
        self.takeOut = False
        self.main = ""
        self.drink = ""

    def getCost(self) -> float:
        return self.cost

    def setCost(self, cost: float) -> None:
        self.cost = cost

    def getTakeOut(self) -> bool:
        return self.takeOut

    def setTakeOut(self, takeOut: bool) -> None:
        self.takeOut = takeOut

    def getMain(self) -> str:
        return self.main

    def setMain(self, main: str) -> None:
        self.main = main

    def getDrink(self) -> str:
        return self.drink

    def setDrink(self, drink: str) -> None:
        self.drink = drink


class MealBuilder:
    
    def __init__(self):
        self._cost = 0.0
        self._takeOut = False
        self._main = ''
        self._drink = ''

    def addCost(self, cost: float) -> 'MealBuilder':
        self._cost = cost
    def addTakeOut(self, takeOut: bool) -> 'MealBuilder':
        self._takeOut = takeOut
    def addMainCourse(self, main: str) -> 'MealBuilder':
        self._main = main
    def addDrink(self, drink: str) -> 'MealBuilder':
        self._drink = drink
    def build(self) -> Meal:
        meal = Meal()
        meal.setCost(
            self._cost
        )
        meal.setTakeOut(
            self._takeOut
        )
        meal.setMain(
            self._main
        )
        meal.setDrink(
            self._drink
        )
        return meal
