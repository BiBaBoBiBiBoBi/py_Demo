# oop : object oriented programming
#   程序长度和逻辑增加。将编程中涉及性质抽象成对象。
#   类是创建的示例模板，对象是类的实例
#   封装 ， 继承 ， 多态
# pp : Procedural Programming
#   将要做的任务拆解成步骤，分布编程


class MyFistPythonClass:
    # some code
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self, word):
        print("Meow~" * self.age)
        print(f"{word}")


cat_1 = MyFistPythonClass("Jojo", 4, "yellow")
cat_1.speak("Wan!")
# print(cat1)
