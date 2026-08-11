import enum


class Op(enum.IntEnum):
    ADD = 1
    MUL = 2
    INP = 3
    OUT = 4
    JIT = 5
    JIF = 6
    SLT = 7
    SEQ = 8
    HCF = 99


def parse_modes(literal: str) -> list[int]:
    modes = list(range(3))

    modes[0] = int(literal[2])
    modes[1] = int(literal[1])
    modes[2] = int(literal[0])

    return modes


def unary_parameter(mem: list[int], ip: int, modes: list[int]) -> int:
    if modes[0] == 1:
        return mem[ip + 1]
    else:
        return mem[mem[ip + 1]]


def binary_parameters(mem: list[int], ip: int, modes: list[int]) -> tuple[int, int]:
    left: int = 0
    right: int = 0

    if modes[0] == 1:
        left = mem[ip + 1]
    else:
        left = mem[mem[ip + 1]]

    if modes[1] == 1:
        right = mem[ip + 2]
    else:
        right = mem[mem[ip + 2]]

    return left, right


def execute(
    mem: list[int], inp: list[int] | None = None
) -> tuple[list[int], list[int]]:
    if inp is None:
        inp = list()

    out = list()

    # instruction pointer
    ip = 0

    while True:
        instruction = mem[ip]
        literal = f"{instruction:05d}"
        modes = parse_modes(literal)
        opcode = instruction % 100

        match opcode:
            case Op.ADD:
                left, right = binary_parameters(mem, ip, modes)
                mem[mem[ip + 3]] = left + right
                ip = ip + 4
            case Op.MUL:
                left, right = binary_parameters(mem, ip, modes)
                mem[mem[ip + 3]] = left * right
                ip = ip + 4
            case Op.INP:
                value = inp.pop(0)
                mem[mem[ip + 1]] = value
                ip = ip + 2
            case Op.OUT:
                value = unary_parameter(mem, ip, modes)
                out.append(value)
                ip = ip + 2
            case Op.JIT:
                left, right = binary_parameters(mem, ip, modes)
                if left != 0:
                    ip = right
                else:
                    ip = ip + 3
            case Op.JIF:
                left, right = binary_parameters(mem, ip, modes)
                if left == 0:
                    ip = right
                else:
                    ip = ip + 3
            case Op.SLT:
                left, right = binary_parameters(mem, ip, modes)
                if left < right:
                    mem[mem[ip + 3]] = 1
                else:
                    mem[mem[ip + 3]] = 0
                ip = ip + 4
            case Op.SEQ:
                left, right = binary_parameters(mem, ip, modes)
                if left == right:
                    mem[mem[ip + 3]] = 1
                else:
                    mem[mem[ip + 3]] = 0
                ip = ip + 4
            case Op.HCF:
                return mem, out

    return mem, out
