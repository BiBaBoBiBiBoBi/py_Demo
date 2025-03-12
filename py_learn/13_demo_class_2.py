# inherit
class Person:
    def __init__(self,name,sex):
        self.name = name
        self.sex=sex

    def breath(self):
        print(f"{self.name} inhale some air...")

    def pooping(self):
        print(f"{self.name} taking a big dump ~~")

class LeeJohn(Person):
    # 在 Python 中，带有默认值的参数（可选参数）必须放在没有默认值的参数（必选参数）之后，否则会引发语法错误。
    def __init__(self,name="LeeJohn",sex="male"):
        super().__init__(name,sex)
        self.ability = ["work","fishing","swim"]

    def work(self):
        print(f"I'm {self.name},and I work everyday.")


lee = LeeJohn()
print(f"Lee's info:\n\t{lee.sex} , {lee.name} , {lee.ability}")
lee.pooping()
