from jinja2 import Template, Environment, FileSystemLoader
import os

class BotTemplateGenerator:
    """
    Bot Template Generator
    ----------------------
    
    Renders templates for CLI AI assistant bots based on relative class and file name
    Template instructions should provide params related to the assistant tasks

    EXAMPLE:
    # Initialize generators with appropriate template files
        auto_bot_generator = BotTemplateGenerator(template_file='./auto_code_bot.jinja2')
        auto_bot_generator.generate_auto_bots('JinjaRefinement', 'jinja_refinement')

    # Generate CLI endpoint code
        cli_generator = BotTemplateGenerator(template_file='./endpoint_cli_tool.jinja2')
        cli_generator.generate_cli_endpoint('JinjaRefinement', 'jinja_refinement')
    
    """
    def __init__(self, template_string=None, template_file=None):
        """
        Initialize the JinjaTemplateGenerator with a template string or a template file.
        
        :param template_string: A string containing the Jinja template (optional).
        :param template_file: A path to a file containing the Jinja template (optional).
        """
        if template_string:
            self.template = Template(template_string)
        elif template_file:
            self.load_template_from_file(template_file)
        else:
            raise ValueError("Either template_string or template_file must be provided.")

    def load_template_from_file(self, template_file):
        """
        Load a Jinja template from a file.
        
        :param template_file: Path to the template file.
        """
        assert os.path.isfile(template_file), f"Template file {template_file} does not exist."
        env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)))
        self.template = env.get_template(os.path.basename(template_file))

    def render(self, **kwargs):
        """
        Render the template with the provided keyword arguments.
        
        :param kwargs: Keyword arguments to render the template.
        :return: Rendered template as a string.
        """
        assert isinstance(kwargs, dict), "Arguments must be provided as a dictionary."
        return self.template.render(**kwargs)

    def generate_auto_bots(self, base_class_name, base_file_name):
        """
        Generate auto bots code using the specified class name.
        
        :param base_class_name: The name of the class to be used in the template.
        """
        try:
            self.load_template_from_file('./auto_code_bot.jinja2')
            rendered_code = self.render(base_class_name=base_class_name)
            self.write_to_file(f'src/auto_code/{base_file_name.lower()}_bot.py', rendered_code)
        except Exception as e:
            print(f"Error generating auto bots: {e}")

    def generate_cli_endpoint(self, base_class_name, base_file_name):
        """
        Generate CLI endpoint code using the specified file name.
        
        :param base_class_name: The name of the class to be used in the template.
        :param base_file_name: The name of the file to be used in the template.
        """
        try:
            self.load_template_from_file('./endpoint_cli_tool.jinja2')
            rendered_code = self.render(base_file_name=base_file_name, base_class_name=base_class_name)
            self.write_to_file(f'src/cli/{base_file_name.lower()}.py', rendered_code)
        except Exception as e:
            print(f"Error generating CLI endpoint: {e}")

    def write_to_file(self, file_path, content):
        """
        Write the rendered content to a specified file.
        
        :param file_path: The path to the file where content will be written.
        :param content: The content to write to the file.
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Generated file: {file_path}")

if __name__ == "__main__":
    BotTemplateGenerator()
    # EXAMPLE:

    # Initialize generators with appropriate template files
    # auto_bot_generator = BotTemplateGenerator(template_file='./auto_code_bot.jinja2')
    # auto_bot_generator.generate_auto_bots('JinjaRefinement', 'jinja_refinement')
    
    # # Generate CLI endpoint code
    # cli_generator = BotTemplateGenerator(template_file='./endpoint_cli_tool.jinja2')
    # cli_generator.generate_cli_endpoint('JinjaRefinement', 'jinja_refinement')