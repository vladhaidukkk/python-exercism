import re

def translate(text):
    def translate_word(word):
        if re.match("[aeiou]|xr|yt", word):
            return word + "ay"
        if (m := re.match("[^aeiou]*qu|[^aeiou]+(?=[aeiouy])", word)):
            return word.replace(m.group(), "", 1) + m.group() + "ay"

    return " ".join(translate_word(word) for word in text.split())
