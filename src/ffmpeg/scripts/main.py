import typer

from .manual.cli import app as manual_app
from .parse_help.cli import app as parse_help_app

app = typer.Typer()


app.add_typer(parse_help_app, name="parse-help")
app.add_typer(manual_app, name="manual")

if __name__ == "__main__":
    app()
