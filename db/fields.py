class Field:
    def __init__(self, required=True, default=None):
        self.required = required
        self.default = default
        self.value = None
        self.errors = []

    # def __str__(self, type:None):
    #     return self.value

    def __str__(self):
        return self.value

    def get(self):
        return self.value

    def __set__(self, value=None):
        if value == None:
            self.value = self.default
        else:
            self.value = value

    def set(self, value=None):
        if not value:
            self.value = self.default
        else:
            self.value = value

    def validate(self):
        if not self.value and self.required:
            self.errors.append(self._name + ' is Required')
            return False
        return True

    def error_messages(self):
        return self.errors


class CharField(Field):

    def set(self, value=''):
        if not isinstance(value, str):
            self.errors.append(self._name + ' should be string')
        super().__set__(value)

    def validate(self):
        super().validate()
        if not isinstance(self.value, str) and self.value=='':
            self.errors.append(self._name + ' Should be string')
            return False
        return True

class FloatField(Field):

    def set(self, value=0.00):
        if not isinstance(value, float):
            self.errors.append(self._name + ' Should be decimal')
        super().__set__(float(value))

    def validate(self):
        super().validate()
        if not isinstance(self.value, float):
            self.errors.append(self._name + ' Should be decimal')
            return False
        return True

    def __str__(self):
        return str(self.value)

class BooleanField(Field):

    def set(self, value=False):
        if not isinstance(self.value, bool):
            self.errors.append(self._name + ' should be True or False')
        super().__set__(value)

    def validate(self):
        super().validate()
        if not isinstance(self.value, bool):
            self.errors.append(self._name + ' Should be True or False')
            return False
        return True

    def __str__(self):
        return str(self.value)

class IntegerField(Field):

    def set(self, value=0):
        if not isinstance(value, int):
            self.errors.append(self._name + ' Should be integer')
        super().__set__(value)

    def validate(self):
        super().validate()
        if not isinstance(self.value, int):
            self.errors.append(self._name + ' Should be integer')
            return False
        return True

    def __str__(self):
        return str(self.value)