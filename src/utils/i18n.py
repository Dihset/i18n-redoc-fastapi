import gettext
from contextvars import ContextVar

LANGUAGES = ["en", "ru"]

translation = {lang: gettext.translation("messages", localedir="translations", languages=[lang]) for lang in LANGUAGES}

language = ContextVar("language", default="en")


def get_translation():
    return translation.get(language.get(), translation["en"])


def get_text(text: str):
    print(text, language.get(), get_translation().gettext(text))
    return get_translation().gettext(text)


_ = get_text
