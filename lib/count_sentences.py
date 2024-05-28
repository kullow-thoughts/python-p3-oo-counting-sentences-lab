class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        replaced_value = self.value.replace('!', '.').replace('?', '.')
        new_sentences = replaced_value.split('.')
        sentences = []
        for s in new_sentences:
            stripped_sentence = s.strip()
            if stripped_sentence:
                sentences.append(stripped_sentence)
        return len(sentences)



