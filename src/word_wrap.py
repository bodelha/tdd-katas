class Wrapper:
    def wrap(self, string, col_num) -> str:
        result = string[:col_num]
        for i in range(1, round(len(string)/col_num + 0.5)):
            result += f"\n{string[col_num*i:col_num*(i+1)]}"
        result = result.replace("\n ", "\n")
        result = result.replace(" \n", "\n")
        return result