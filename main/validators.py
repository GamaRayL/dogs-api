from rest_framework.exceptions import ValidationError


class DogNameValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value, *args, **kwargs):
        valid_words = ['продам', 'крипта', 'ставки']
        tmp_value = dict(value).get(self.field).lower()

        for word in valid_words:
            if word in tmp_value:
                raise ValidationError('Запрещены рекламные слова!')