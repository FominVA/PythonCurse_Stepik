from copy import deepcopy

class Selfie:
    def __init__(self):
        self._state = []

    def save_state(self):
        current_state = deepcopy(self.__dict__)
        self._state.append(current_state)

    def recover_state(self, index):
        if  0 <= index < len(self._state):
            new_obj = Selfie()
            new_obj.__dict__.update(deepcopy(self._state[index]))
            return new_obj
        else:
            new_obj = Selfie()
            new_obj.__dict__.update(self.__dict__)
            return new_obj

    def n_states(self):
        return len(self._state)

obj = Selfie()

print(obj.n_states())

obj.x = 0
obj.save_state()
obj.x = 1
obj.save_state()
obj.x = 2
obj.save_state()

print(obj.n_states())

obj1 = obj.recover_state(1)

print(obj1.n_states())
print(obj.n_states())