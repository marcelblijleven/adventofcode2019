class Intcode:
    def __init__(self, memory, noun=None, verb=None, input_list=[]):
        self.memory = memory
        self.input_list = input_list
        self.output = []

        if noun is not None and verb is not None:
            self.memory[1] = noun
            self.memory[2] = verb

    def execute(self):
        init_instruction = self.memory[0]
        first_opcode = int(init_instruction[-2:])
        initial_step_size = self.__step_size(first_opcode)

        def take_chunk(start=0):
            instruction = self.memory[start]
            opcode = int(instruction[-2:])
            step_size = self.__step_size(opcode)

            try:
                chunk = self.memory[start: start + step_size]
            except IndexError:
                return self.memory

            if opcode == 99:
                return self.memory, ''.join(self.output)

            if opcode == 1:
                self._execute_sum(chunk)
            elif opcode == 2:
                self._execute_multiply(chunk)
            elif opcode == 3:
                self._execute_input(chunk)
            elif opcode == 4:
                self._execute_output(chunk)

            if instruction.endswith('4'):
                print(chunk)

            return take_chunk(start=start + step_size)

        return take_chunk()

    def _execute_sum(self, chunk):
        instruction = chunk[0]
        param_one = int(chunk[1])
        param_two = int(chunk[2])
        destination = int(chunk[3])
        p1_mode, p2_mode, _ = self._get_param_modes(instruction)

        value_one = param_one if p1_mode == 'immediate' else self.memory[param_one]
        value_two = param_two if p2_mode == 'immediate' else self.memory[param_two]
        self.memory[destination] = str(int(value_one) + int(value_two))

    def _execute_multiply(self, chunk):
        instruction = chunk[0]
        param_one = int(chunk[1])
        param_two = int(chunk[2])
        destination = int(chunk[3])
        p1_mode, p2_mode, _ = self._get_param_modes(instruction)

        value_one = param_one if p1_mode == 'immediate' else self.memory[param_one]
        value_two = param_two if p2_mode == 'immediate' else self.memory[param_two]
        self.memory[destination] = str(int(value_one) * int(value_two))

    def _execute_input(self, chunk):
        param_one = int(chunk[1])
        next_input = self.input_list.pop(0)
        self.memory[param_one] = next_input

    def _execute_output(self, chunk):
        instruction = chunk[0]
        param_one = int(chunk[1])
        p1_mode, _, _ = self._get_param_modes(instruction)

        self.output.append(
            str(param_one) if p1_mode == 'immediate' else self.memory[param_one]
        )

    def _get_param_modes(self, instruction):
        """
        ABCDE
         1002

        DE - two-digit opcode,      02 == opcode 2
         C - mode of 1st parameter,  0 == position mode
         B - mode of 2nd parameter,  1 == immediate mode
         A - mode of 3rd parameter,  0 == position mode,
                                          omitted due to being a leading zero
        """

        param_one = self.__read_parameter(instruction[-3:-2])
        param_two = self.__read_parameter(instruction[-4:-3])
        param_three = self.__read_parameter(instruction[-5:-4])
        return param_one, param_two, param_three

    @staticmethod
    def __read_parameter(parameter):
        try:
            if int(parameter) == 1:
                return 'immediate'
        except ValueError:
            pass  # Parameter not present in opcode

        return 'position'

    @staticmethod
    def __step_size(opcode):
        if opcode in [1, 2]:
            return 4
        elif opcode in [3, 4]:
            return 2
        elif opcode == 99:
            return 0  # End of program

        raise ValueError('Cannot calculate step size for opcode', opcode)
