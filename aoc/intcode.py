import enum


class Op(enum.IntEnum):
    ADD = 1
    MUL = 2
    HCF = 99


def execute(mem: list[int]) -> list[int]:
    # instruction pointer
    ip = 0

    while True:
        match mem[ip]:
            case Op.ADD:
                mem[mem[ip + 3]] = mem[mem[ip + 1]] + mem[mem[ip + 2]]
                ip = ip + 4
            case Op.MUL:
                mem[mem[ip + 3]] = mem[mem[ip + 1]] * mem[mem[ip + 2]]
                ip = ip + 4
            case Op.HCF:
                return mem

    return mem
