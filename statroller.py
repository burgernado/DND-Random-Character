import d20


class MyStringifier(d20.SimpleStringifier):
    def _stringify(self, node):
        if not node.kept:
            return 'X'
        return super()._stringify(node)

    def _str_expression(self, node):
        return f"The result of the roll was {int(node.total)}"


result = d20.roll("4d6e6kh3", stringifier=MyStringifier())
str(result)
