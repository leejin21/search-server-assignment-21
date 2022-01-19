class Language:
    languages = ["EN", "KR", "JP"]

    @classmethod
    def is_valid_language(cls, lang):
        return lang in cls.languages

    @classmethod
    def display(cls):
        return cls.languages