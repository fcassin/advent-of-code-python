import collections
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


class Signal(enum.IntEnum):
    INP = 1
    EOT = 2
    HCF = 99


class IntCodeVM:
    def __init__(self, name):
        self.name = name
        self.ip = 0
        self.inputs = collections.deque()
        self.outputs = collections.deque()

    def memory(self, memory):
        self.mem = memory

    def input(self, input):
        self.inputs.append(input)

    def run(self):
        while True:
            instruction = self.mem[self.ip]
            literal = f"{instruction:05d}"
            modes = parse_modes(literal)
            opcode = instruction % 100

            match opcode:
                case Op.ADD:
                    left, right = binary_parameters(self.mem, self.ip, modes)
                    self.mem[self.mem[self.ip + 3]] = left + right
                    self.ip = self.ip + 4
                case Op.MUL:
                    left, right = binary_parameters(self.mem, self.ip, modes)
                    self.mem[self.mem[self.ip + 3]] = left * right
                    self.ip = self.ip + 4
                case Op.INP:
                    if len(self.inputs) == 0:
                        yield Signal.INP
                        # return

                    value = self.inputs.popleft()
                    self.mem[self.mem[self.ip + 1]] = value
                    self.ip = self.ip + 2
                case Op.OUT:
                    value = unary_parameter(self.mem, self.ip, modes)
                    self.outputs.append(value)
                    self.ip = self.ip + 2
                case Op.JIT:
                    left, right = binary_parameters(self.mem, self.ip, modes)
                    if left != 0:
                        self.ip = right
                    else:
                        self.ip = self.ip + 3
                case Op.JIF:
                    left, right = binary_parameters(self.mem, self.ip, modes)
                    if left == 0:
                        self.ip = right
                    else:
                        self.ip = self.ip + 3
                case Op.SLT:
                    left, right = binary_parameters(self.mem, self.ip, modes)
                    if left < right:
                        self.mem[self.mem[self.ip + 3]] = 1
                    else:
                        self.mem[self.mem[self.ip + 3]] = 0
                    self.ip = self.ip + 4
                case Op.SEQ:
                    left, right = binary_parameters(self.mem, self.ip, modes)
                    if left == right:
                        self.mem[self.mem[self.ip + 3]] = 1
                    else:
                        self.mem[self.mem[self.ip + 3]] = 0
                    self.ip = self.ip + 4
                case Op.HCF:
                    yield Signal.HCF
                    # return

        yield Signal.EOT
        # return


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
    """
    execute will spin up a VM and expect it to have enough input to go to HCF
    without being interrupted
    """
    if inp is None:
        inp = list()

    vm = IntCodeVM("unnamed")
    for input in inp:
        vm.input(input)

    vm.memory(mem)

    for signal in vm.run():
        if signal != Signal.HCF:
            raise Exception("received unexpected signal")
        else:
            break

    out = list()
    for value in vm.outputs:
        out.append(value)

    return vm.mem, out
