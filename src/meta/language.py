class Language:
    languages = ["EN", "KR", "JP"]

    @staticmethod
    def is_valid_language(self, lang):
        return lang in self.languages
