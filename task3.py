class stack:
    def	__init__(self):
        self.data = list()
    def push(self, x):
        self.data.append(x)

    def pop(self):
        self.data.pop()

    def top(self):
        if self.empty():
            return None
        return self.data[-1]

    def empty(self):
        return len(self.data) == 0


openning_brackets = ['(', '[', '{']
closing_brackets = [')', ']', '}']

def check_valid_bracket(expression):
    if expression[0] not in openning_brackets:
        return False

    prio = {'(':1, '[': 2, '{': 3,
            ')':1, ']': 2, '}': 3}
    s = stack()

# correct opening  and closing of brackets
    s.push(expression[0])
    for idx in range(1, len(expression)):
        if expression[idx] in openning_brackets:
            s.push(expression[idx])

        if expression[idx] in closing_brackets:
            if prio[expression[idx]] != prio[s.top()]:
                return False
            s.pop()
            if s.empty() and idx  != len(expression) -1:
                return False

# correct correlation between brackets
    cur_prio = prio[expression[0]]
    for letter in expression[1:]:
        if letter in openning_brackets:
            if (cur_prio - prio[letter] ) != 1:
                return False
            else:
                cur_prio -= 1
        elif letter in closing_brackets:
            cur_prio += 1
    return True

def calculate(expression):
    if not check_valid_bracket(expression):
        print("NO")
        return None

    if expression[1:-1] == "":
        return 0

    numbers = []
    idx = 1
    while idx < len(expression) and expression[idx] not in openning_brackets+closing_brackets :
        idx += 1
    numbers.append(expression[1:idx])
    closing_bracket_idx = idx
    sub_exprs = []
    #{123[.....]123(...)123}
    if closing_bracket_idx == len(expression) - 1:
        return int(numbers[0])

    while idx < (len(expression)-1):
        s = stack()
        s.push(expression[closing_bracket_idx])

        while not s.empty():
            closing_bracket_idx += 1
            if expression[closing_bracket_idx] in openning_brackets:
                s.push(expression[closing_bracket_idx])
            elif expression[closing_bracket_idx] in closing_brackets:
                s.pop()

        sub_exprs.append(expression[idx:closing_bracket_idx + 1] )
        closing_bracket_idx += 1
        idx = closing_bracket_idx
        while closing_bracket_idx < (len(expression) - 1) and expression[closing_bracket_idx] not in openning_brackets:
            closing_bracket_idx += 1
        numbers.append(expression[idx:closing_bracket_idx])
        idx = closing_bracket_idx
    numbers = sum(map(lambda x: int(x), filter(lambda x: x!="", numbers)))
    expressions = 2 * sum(map(lambda x: calculate(x), filter(lambda x: x !="",sub_exprs )))
    return numbers + expressions

if __name__ == "__main__":
    expr = input()
    print(calculate(expr))