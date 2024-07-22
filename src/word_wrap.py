class Wrapper:
    def wrap(self, string, col_num) -> str:
        result = string[:col_num]
        if len(string) <= col_num:
            return result
        space = string.rfind(' ', 0, col_num + 1)
        if space >=0:
            return result[:space] + "\n" + self.wrap(string[space + 1:], col_num)
        result = result + "\n" + self.wrap(string[col_num:], col_num)
        return result
    