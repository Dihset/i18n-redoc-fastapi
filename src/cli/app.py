import typer

from src.cli.i18n import generate_redoc
from src.cli.run_web import run_web

typer_app = typer.Typer()
typer_app.command()(generate_redoc)
typer_app.command()(run_web)
