class Intcode:
    def __init__(self, memory, noun=None, verb=None, inputs=[]):
        self.memory = memory
        self.inputs = inputs
        self.output = []

        if noun is not None and verb is not None:
            self.memory[1] = noun
            self.memory[2] = verb

    def execute(self):
        cursor = 0

        while cursor < len(self.memory):
            instruction = str(self.memory[cursor])
            opcode = int(instruction[-2:])
            p1_mode, p2_mode, p3_mode = self._get_param_modes(instruction)

            if opcode in [1, 2, 7, 8]:
                chunk = self.memory[cursor:cursor + 4]
                parameter_one = chunk[1]
                parameter_two = chunk[2]
                destination = chunk[3]
                value_one = parameter_one if p1_mode == 'immediate' else self.memory[parameter_one]
                value_two = parameter_two if p2_mode == 'immediate' else self.memory[parameter_two]

                if opcode == 1:
                    self.memory[destination] = value_one + value_two
                elif opcode == 2:
                    self.memory[destination] = value_one * value_two
                elif opcode == 7:
                    output = 1 if value_one < value_two else 0
                    self.memory[destination] = output
                elif opcode == 8:
                    output = 1 if value_one == value_two else 0
                    self.memory[destination] = output
                else:
                    raise ValueError(f'Incorrect opcode "{opcode}"')
                cursor += 4
            elif opcode == 2:
                chunk = self.memory[cursor:cursor + 4]
                parameter_one = chunk[1]
                parameter_two = chunk[2]
                destination = chunk[3]
                value_one = parameter_one if p1_mode == 'immediate' else self.memory[parameter_one]
                value_two = parameter_two if p2_mode == 'immediate' else self.memory[parameter_two]
                self.memory[destination] = value_one * value_two
                cursor += 4
            elif opcode == 3:
                chunk = self.memory[cursor:cursor + 2]
                try:
                    next_input = self.inputs.pop(0)
                except IndexError:
                    next_input = input('Provide input: ')

                self.memory[chunk[1]] = next_input
                cursor += 2
            elif opcode == 4:
                chunk = self.memory[cursor:cursor + 2]
                param = chunk[1]
                self.output.append(param if p1_mode == 'immediate' else self.memory[param])
                cursor += 2
            elif opcode in [5, 6]:
                chunk = self.memory[cursor:cursor + 3]
                param_one = chunk[1]
                param_two = chunk[2]
                value_one = param_one if p1_mode == 'immediate' else self.memory[param_one]
                value_two = param_two if p2_mode == 'immediate' else self.memory[param_two]

                if opcode == 5 and value_one != 0:
                    # Jump to position
                    cursor = value_two
                elif opcode == 6 and value_one == 0:
                    # Jump to position
                    cursor = value_two
                else:
                    cursor += 3
            elif opcode == 99:
                return self.output
            else:
                raise ValueError(f'Unknown instruction at cursor {cursor}: {instruction}')

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
