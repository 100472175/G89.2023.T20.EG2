from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class FileHeaderChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'file-header-checker'
    priority = -1
    msgs = {
        'W9999': ('Missing file header', 'missing-file-header', 'Missing required file header comments'),
        'W8888': ('Missing class header', 'missing-class-header', 'Missing required class header comments')
    }
    options = ()

    def visit_module(self, node):
        file_header = [
            'Name of the file',
            '@Author: ',
            '@version: ',
            '@Date: ',
            '@Creation: ',
            'Instructions: '
        ]
        class_header = [
            'Name of the class',
            'Description:'
        ]
        class_found = False

        # check if file has class definition
        for child in node.get_children():
            if child.is_class():
                class_found = True
                break

        # check file header
        for i, line in enumerate(node.stream().lines):
            if i >= len(file_header):
                break
            if line.strip() != file_header[i]:
                self.add_message('missing-file-header', line=line)

        # check class header
        if class_found:
            class_def = node.get_children()[0]
            class_doc = class_def.doc
            if class_doc is None or not all(line.startswith(tuple(class_header)) for line in class_doc.split('\n')):
                self.add_message('missing-class-header', node=class_def)

def register(linter):
    linter.register_checker(FileHeaderChecker(linter))
