import sys


def interprete(program):
    pos = 0
    registers = [0]
    pointer = 0
    while pos < len(program):
        if program[pos] == '>':
            pointer += 1
            if len(registers) <= pointer:
                registers.append(0)
        elif program[pos] == '<':
            pointer -= 1
        elif program[pos] == '+':
            registers[pointer] += 1
        elif program[pos] == '-':
            registers[pointer] -= 1
        elif program[pos] == '.':
            print(chr(registers[pointer]), end="")
        elif program[pos] == ',':
            registers[pointer] = ord(sys.stdin.read(1))
        elif program[pos] == '[':
            if registers[pointer] == 0:
                new_pos = pos + 1
                temp = 0
                found = False
                while not found:
                    if program[new_pos] == '[':
                        temp += 1
                    elif program[new_pos] == ']' and temp > 0:
                        temp -= 1
                    elif program[new_pos] == ']' and temp == 0:
                        found = True
                        pos = new_pos
                    new_pos += 1
        elif program[pos] == ']':
            new_pos = pos - 1
            temp = 0
            found = False
            while not found:
                if program[new_pos] == ']':
                    temp += 1
                elif program[new_pos] == '[' and temp > 0:
                    temp -= 1
                elif program[new_pos] == '[' and temp == 0:
                    found = True
                    pos = new_pos - 1
                new_pos -= 1
        pos += 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit()

    f = open(sys.argv[1], 'r')
    interprete(f.read())
    f.close()
