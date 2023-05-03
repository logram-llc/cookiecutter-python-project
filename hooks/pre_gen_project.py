{{ cookiecutter.update({ "slug": cookiecutter.project.lower().replace(" ", "_").replace("-", "_").replace(".", "_").strip() })}}
{{ cookiecutter.update({"entrypoint": cookiecutter.slug.replace("_", "-") })}}
{{ cookiecutter.update({ "py_version": "py" + cookiecutter.python_version.replace(".", "") })}}