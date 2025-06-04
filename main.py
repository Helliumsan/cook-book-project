import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

class LoadingScreen(QDialog):
    def __init__(self):
        super(LoadingScreen,self).__init__()
        self.setFixedSize(1920,1080)
        loadUi('starting_screen.ui',self)
        self.my_recipes_button.clicked.connect(self.GoToRecipes)
        self.exit_button.clicked.connect(app.quit)

    def GoToRecipes(self):
        widget.setCurrentIndex(1)

class MyRecipes(QDialog):
    def __init__(self):
        super(MyRecipes,self).__init__()
        self.setFixedSize(1920,1080)
        loadUi('my recipes.ui',self)
        self.exit_button.clicked.connect(self.GoToLoadingScreen)
        self.marshmallow_button.clicked.connect(self.OpenMarshmallow)
        self.cookies_button.clicked.connect(self.OpenCookie)
        self.pancakes_button.clicked.connect(self.OpenPancakes)
        self.muffin_button.clicked.connect(self.OpenMuffin)
        self.lemon_button.clicked.connect(self.OpenPastry)
        self.roll_button.clicked.connect(self.OpenBiscuit)
        self.potato_button.clicked.connect(self.OpenKartoshka)
        self.brownie_button.clicked.connect(self.OpenBrownie)

    def GoToLoadingScreen(self):
        widget.setCurrentIndex(0)

    def OpenMarshmallow(self):
        widget.setCurrentIndex(2)

    def OpenCookie(self):
        widget.setCurrentIndex(3)

    def OpenPancakes(self):
        widget.setCurrentIndex(4)

    def OpenMuffin(self):
        widget.setCurrentIndex(5)

    def OpenPastry(self):
        widget.setCurrentIndex(6)

    def OpenBiscuit(self):
        widget.setCurrentIndex(7)

    def OpenKartoshka(self):
        widget.setCurrentIndex(8)

    def OpenBrownie(self):
        widget.setCurrentIndex(9)

#__________________________________________________________


class Marshmallow(QDialog):
    def __init__(self):
        super(Marshmallow,self).__init__()
        self.setFixedSize(1920,1080)
        loadUi('marshmallow.ui',self)
        self.exit_button.clicked.connect(self.GoToRecipes)

    def GoToRecipes(self):
        widget.setCurrentIndex(1)


class ChocolateChipCookie(QDialog):
    def __init__(self):
        super(ChocolateChipCookie,self).__init__()
        self.setFixedSize(1920,1080)
        loadUi('cookies.ui',self)
        self.exit_button.clicked.connect(self.GoToRecipes)

    def GoToRecipes(self):
        widget.setCurrentIndex(1)


class PancakesWithMilk(QDialog):
    def __init__(self):
        super(PancakesWithMilk,self).__init__()
        self.setFixedSize(1920,1080)
        loadUi('pancakes.ui',self)
        self.exit_button.clicked.connect(self.GoToRecipes)

    def GoToRecipes(self):
        widget.setCurrentIndex(1)


class ChocolateMuffin(QDialog):
    def __init__(self):
        super(ChocolateMuffin,self).__init__()
        self.setFixedSize(1920,1080)
        loadUi('choco muffin.ui',self)
        self.exit_button.clicked.connect(self.GoToRecipes)

    def GoToRecipes(self):
        widget.setCurrentIndex(1)


class LemonPastry(QDialog):
    def __init__(self):
        super(LemonPastry,self).__init__()
        self.setFixedSize(1920,1080)
        loadUi('lemon pastry.ui',self)
        self.exit_button.clicked.connect(self.GoToRecipes)

    def GoToRecipes(self):
        widget.setCurrentIndex(1)


class BiscuitRoll(QDialog):
    def __init__(self):
        super(BiscuitRoll,self).__init__()
        self.setFixedSize(1920,1080)
        loadUi('biscuit_roll.ui',self)
        self.exit_button.clicked.connect(self.GoToRecipes)

    def GoToRecipes(self):
        widget.setCurrentIndex(1)


class KartoshkaCake(QDialog):
    def __init__(self):
        super(KartoshkaCake,self).__init__()
        self.setFixedSize(1920,1080)
        loadUi('potato.ui',self)
        self.exit_button.clicked.connect(self.GoToRecipes)

    def GoToRecipes(self):
        widget.setCurrentIndex(1)


class Brownie(QDialog):
    def __init__(self):
        super(Brownie,self).__init__()
        self.setFixedSize(1920,1080)
        loadUi('brownie.ui',self)
        self.exit_button.clicked.connect(self.GoToRecipes)

    def GoToRecipes(self):
        widget.setCurrentIndex(1)

#__________________________________________________________


app = QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
widget.x=0
widget.y=0
loading_screen=LoadingScreen()
my_recipes=MyRecipes()
marshmallow=Marshmallow()
cookies=ChocolateChipCookie()
pancakes=PancakesWithMilk()
muffin=ChocolateMuffin()
pastry=LemonPastry()
biscuit=BiscuitRoll()
kartoshka=KartoshkaCake()
brownie=Brownie()

widget.addWidget(loading_screen)
widget.addWidget(my_recipes)
widget.addWidget(marshmallow)
widget.addWidget(cookies)
widget.addWidget(pancakes)
widget.addWidget(muffin)
widget.addWidget(pastry)
widget.addWidget(biscuit)
widget.addWidget(kartoshka)
widget.addWidget(brownie)

widget.show()

sys.exit(app.exec_())

