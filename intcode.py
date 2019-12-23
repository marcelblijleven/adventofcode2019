class Intcode:
    def __init__(self, memory, inputs, noun=None, verb=None):
        self.cursor = 0
        self.memory = memory
        self.inputs = inputs
        self.output = None
        self.halted = False

        if noun is not None and verb is not None:
            self.memory[1] = noun
            self.memory[2] = verb

    def get_parameter_value(self, param, mode):
        return param if mode == 1 else self.memory[param]

    def sum(self, value_one, value_two, destination):
        # opcode 1
        self.memory[destination] = value_one + value_two

    def multiply(self, value_one, value_two, destination):
        # opcode 2
        self.memory[destination] = value_one * value_two

    def process_input(self, param):
        # opcode 3
        self.memory[param] = self.inputs.pop(0)

    def process_output(self, value):
        # opcode 4
        self.output = value

    def jump_if_true(self, value_one, value_two):
        # opcode 5
        self.cursor = value_two if value_one != 0 else self.cursor + 3

    def jump_if_false(self, value_one, value_two):
        # opcode 6
        self.cursor = value_two if value_one == 0 else self.cursor + 3

    def less_than(self, value_one, value_two, destination):
        # opcode 7
        self.memory[destination] = 1 if value_one < value_two else 0

    def equal(self, value_one, value_two, destination):
        # opcode 8
        self.memory[destination] = 1 if value_one == value_two else 0

    def execute(self):
        while self.cursor < len(self.memory) and not self.halted:
            opcode, p1mode, p2mode, p3mode = process_instruction(
                self.memory[self.cursor]
            )

            if opcode in [1, 2, 7, 8]:
                chunk = self.memory[self.cursor:self.cursor + 4]
                value_one = self.get_parameter_value(chunk[1], p1mode)
                value_two = self.get_parameter_value(chunk[2], p2mode)
                destination = chunk[3]

                if opcode == 1:
                    self.sum(value_one, value_two, destination)
                elif opcode == 2:
                    self.multiply(value_one, value_two, destination)
                elif opcode == 7:
                    self.less_than(value_one, value_two, destination)
                elif opcode == 8:
                    self.equal(value_one, value_two, destination)

                self.cursor += 4
            elif opcode in [3, 4]:
                chunk = self.memory[self.cursor:self.cursor + 2]
                if opcode == 3:
                    self.process_input(chunk[1])
                elif opcode == 4:
                    value = self.get_parameter_value(chunk[1], p1mode)
                    self.process_output(value)

                self.cursor += 2
            elif opcode in [5, 6]:
                chunk = self.memory[self.cursor:self.cursor + 3]
                value_one = self.get_parameter_value(chunk[1], p1mode)
                value_two = self.get_parameter_value(chunk[2], p2mode)

                if opcode == 5:
                    self.jump_if_true(value_one, value_two)
                elif opcode == 6:
                    self.jump_if_false(value_one, value_two)
            elif opcode == 99:
                self.halted = True
                return self.output
            else:
                raise ValueError(f'Unknown opcode {opcode}')

        return self.output

    @staticmethod
    def _get_param_modes(instruction):
        """
        ABCDE
         1002

        DE - two-digit opcode,      02 == opcode 2
         C - mode of 1st parameter,  0 == position mode
         B - mode of 2nd parameter,  1 == immediate mode
         A - mode of 3rd parameter,  0 == position mode,
                                          omitted due to being a leading zero
        """
        def read_parameter(parameter):
            try:
                if int(parameter) == 1:
                    return 'immediate'
            except ValueError:
                pass  # Parameter not present in instruction

            return 'position'

        param_one = read_parameter(instruction[-3:-2])
        param_two = read_parameter(instruction[-4:-3])
        param_three = read_parameter(instruction[-5:-4])
        return param_one, param_two, param_three


def process_instruction(instruction):
    """
    position 0 is parameter 3
    position 1 is parameter 2
    position 2 is parameter 1
    opcode starts at position 3
    returns: opcode, pmode1, pmode2, pmode3
    """
    # Make instruction 5 characters long, pad left with 0
    s_instruction = f'{instruction:05}'

    return (
        int(s_instruction[3:]), int(s_instruction[2]),
        int(s_instruction[1]), int(s_instruction[0]))
