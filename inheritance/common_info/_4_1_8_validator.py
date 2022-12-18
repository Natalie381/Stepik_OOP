class Validator:

    def __call__(self, data):
        return self._is_valid(data)

    def _is_valid(self, data):
        return True


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, int) and self._min_value <= data <= self._max_value:
            return True
        raise ValueError('данные не прошли валидацию')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, float) and self._min_value <= data <= self._max_value:
            return True
        raise ValueError('данные не прошли валидацию')


if __name__ == '__main__':
    integer_validator = IntegerValidator(-10, 10)
    float_validator = FloatValidator(-1, 1)
    res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
    # res2 = float_validator(10)  # исключение ValueError
