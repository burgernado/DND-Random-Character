import d20
counter = 0
counter = counter + 1
resultlist = []


class MyStringifier(d20.SimpleStringifier):
    def _stringify(self, node):
        if not node.kept:
            return 'X'
        return super()._stringify(node)

    def _str_expression(self, node):
        return f"{int(node.total)}"


for i in range(6):
    result = d20.roll("4d6e6kh3", stringifier=MyStringifier())
    resultlist.append(str(result))
