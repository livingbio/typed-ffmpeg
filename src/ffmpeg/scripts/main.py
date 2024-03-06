import typer

from .parse_help.cli import app as parse_help_app

app = typer.Typer()


app.add_typer(parse_help_app, name="parse-help")


if __name__ == "__main__":
    app()
