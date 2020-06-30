import yaml


def pars(file, tag):
    with open(file, encoding="utf-8") as f:
        templates = yaml.safe_load(f)
        start = templates.find(tag)
        end = templates.find('</'+tag)
        value = templates[start:end]
        return value.split(">")[1]