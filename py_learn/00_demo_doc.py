# 私有变量和方法通常以单个下划线开头
# 受保护的成员（变量或方法）通常通过在名称前加单下划线 _ 来表示。这种命名方式是一种约定，表示这些成员是内部使用的，不建议在类的外部直接访问，但 Python 并不会强制限制访问。

# 在 Python 中，私有变量和方法通常通过在名称前加双下划线 __ 来表示。这种命名方式会触发 名称改编（name mangling），使得变量或方法在类的外部不可直接访问。
# 名称改编（Name Mangling）
# Python 会将私有变量和方法的名称改编为 _ClassName__variableName 或 _ClassName__methodName。
# 虽然可以通过改编后的名称访问私有成员，但这并不是推荐的做法，因为它违背了封装的原则。

# Python 的变量名和方法名通常使用 小写字母和下划线 的组合（snake_case）

# 多次重读文件：
# 方法 1：重新打开文件
# 最简单的方式是关闭文件后重新打开它，这样文件指针会重新指向文件开头。
#
# 方法 2：使用 seek() 方法
# 如果你不想关闭文件，可以使用 seek() 方法将文件指针重新定位到文件开头。
# # 将文件指针重新定位到文件开头
# file.seek(0)
#
# 方法 3：将文件内容存储到变量
# 如果你只需要多次访问文件内容，可以在第一次读取时将内容存储到一个变量中，然后多次使用这个变量，而不需要重新读取文件。
# with open("example.txt", "r") as file:
#     content = file.read()
#
# print("First read:", content)
# print("Second read:", content)
# 这种方法适用于文件内容较小的情况，因为它会将整个文件内容加载到内存中。
#
# 方法 4：使用 readlines() 或逐行读取
# 如果你需要多次逐行处理文件内容，可以使用 readlines() 方法将文件内容按行存储到一个列表中，然后多次遍历这个列表。
#
# 如果文件较小且不需要频繁重新读取，可以使用 方法 3 或 方法 4。
# 如果需要多次重新读取文件，建议使用 方法 1（重新打开文件）。
# 如果不想关闭文件，可以使用 方法 2（seek() 方法）。


# with
# 在 Python 中，with 语句用于实现上下文管理（context management），它提供了一种更简洁、更安全的方式来处理资源（如文件、锁、网络连接等）。
# 使用 with 语句可以确保资源在使用后被正确地清理或关闭，即使在代码中发生异常也是如此。


# 模块的顶层作用域（包括 if __name__ == '__main__': 块）中声明的变量和函数是全局的，可以在整个模块中被访问。
'''
全局变量和函数：
在 Python 文件（模块）的顶层作用域中声明的变量和函数是全局的，这意味着它们不属于任何类或函数，可以在整个模块中被访问。
如果在模块的顶层定义了变量或函数，它们就可以在该模块的任何函数或类中被访问，除非在局部作用域中被同名变量或函数遮蔽。
(可以视情况使用 global() , nonlocal() 来获取内外层变量)

if __name__ == '__main__': 块：
if __name__ == '__main__': 块通常用于判断当前模块是被直接运行还是被导入到其他模块中。如果直接运行，__name__ 变量的值为 '__main__'。
在这个块内声明的变量和函数也是全局的，因为它们位于模块的顶层作用域。它们可以被模块中的其他函数或类访问，除非在局部作用域中被遮蔽。
全局变量的修改：
在函数内部修改全局变量时，需要使用 global 关键字声明，否则 Python 会将其视为局部变量。
在类的方法中访问全局变量不需要特殊声明，但如果要修改全局变量，仍然需要在方法内部使用 global 关键字。
全局作用域的限制：
全局变量和函数的作用域限制在定义它们的模块内。不同模块中的全局变量和函数是独立的，不会互相影响。
'''

