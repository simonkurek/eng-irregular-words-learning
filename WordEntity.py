class WordEntity():
    def __init__(self, first_form, second_form, third_form, polish_translation, level):
        self.first_form = first_form
        self.second_form = second_form
        self.third_form = third_form
        self.polish_translation = polish_translation
        self.level = level
        self.points = [0] * 14