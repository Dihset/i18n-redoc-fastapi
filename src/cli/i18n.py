import json

from src.config.base import REDOC_DIR
from src.utils.i18n import LANGUAGES, language


def generate_redoc(lang: str):
    if lang not in LANGUAGES:
        raise ValueError(f"Language {lang} is not supported")
    language.set(lang)

    from src.web import create_app

    app = create_app()
    with open(REDOC_DIR / f"openapi.{lang}.json", "w") as openapi_file:
        json.dump(app.openapi(), openapi_file, indent=4, ensure_ascii=False)
