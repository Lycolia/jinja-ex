from yaml import safe_load as yamlLoad
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('biography', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('index.html')
with open('configs/config.yaml') as fYaml:
    print(template.render(yamlLoad(fYaml)))
