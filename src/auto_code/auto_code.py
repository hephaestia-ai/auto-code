import logging
from typing import List, Union
from core.assistant.core_assistant import CoreAssistant
from cowgirl_ai.error_handler import error_handler
from cowgirl_ai.search.search import Search
# from core.assistant.core_assistant import CoreAssistant

logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d", format="%(levelname)s - %(message)s")

class AutoCode(CoreAssistant):
    """
    Auto Code
    ---------

    Programming assistant 
    """
    def __init__(self):
        super().__init__(assistant_name="Python Code Refinement")
        self.description = "Helpful python code generation and optimization bot"
        self.instructions = """
            No chat response needed, just respond with the code. No backticks needed, will be used for overwriting other .py files.
            Refine every file to include python development best practices.
            Ensure they are optimized. Update them to include new features or libraries
            that would improve functionality. Add assertions and commenting where necessary.
        """
    @error_handler
    def generate(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[
                {"role": "system", "content": self.description},
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": prompt}
            ],
            n=1,
        )
        return completion.choices[0].message.content
    
    @error_handler
    def get_files(self, directory: str, extension: str) -> List[str]:
        """
        Recursively searches a directory for a given file type.
        
        Args:
            directory (str): The directory to search in.
            extension (str): The file extension to search for.

        Returns:
            List[str]: A list of file paths matching the extension.
        """
        search = Search()
        search.search(directory, extension)
        return search.data

    @staticmethod
    def get_file_content(file_path: str) -> Union[str, None]:
        """
        Reads the contents of a file and returns it.

        Args:
            file_path (str): The path to the file.

        Returns:
            Union[str, None]: The contents of the file, or None if an error occurs.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            logging.error(f"Error reading file {file_path}: {e}")
            return None

    @staticmethod
    def write_to_file(file_path: str, data: str, mode: str = 'w') -> bool:
        """
        Writes data to a specified file.

        Args:
            file_path (str): The path to the file.
            data (str): The data to write to the file.
            mode (str): The mode in which to open the file. Defaults to 'w' (write). Use 'a' for appending.

        Returns:
            bool: True if write is successful, otherwise False.
        """
        assert mode in ['w', 'a'], "Mode must be 'w' (write) or 'a' (append)"
        try:
            with open(file_path, mode, encoding='utf-8') as file:
                file.write(data)
            return True
        except IOError as e:
            logging.error(f"Error writing to file {file_path}: {e}")
            return False

    def process_files(self, file_paths: List[str]) -> None:
        """
        Processes each file by refining its content using the assistant.

        Args:
            file_paths (List[str]): List of file paths to process.
        """
        for file_path in file_paths:
            original_content = self.get_file_content(file_path)
            if original_content is not None:
                refined_content = self.generate(prompt=original_content)
                self.write_to_file(file_path, refined_content)

if __name__ == "__main__":
    AutoCode()
