import jinja2

from .settings import settings
from .signature import Filter


def generate_filter_to_method(filter: Filter) -> str:
    return jinja2.Template((settings.template_path / "method.tmpl").read_text()).render(filter=filter)


def generate_class(filters: list[Filter]) -> str:
    methods = []
    for filter in sorted(filters, key=lambda i: i.name):
        try:
            methods.append(generate_filter_to_method(filter))
        except Exception as e:
            print(f"Failed to generate method for {filter.name} Because of {e}")

    return jinja2.Template((settings.template_path / "class.tmpl").read_text()).render(methods=methods)
