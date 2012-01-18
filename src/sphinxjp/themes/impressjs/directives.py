# -*- coding: utf-8 -*-
from docutils import nodes
from sphinx.util.compat import Directive


class impressjs_node(nodes.raw): pass

class Impressjs(Directive):
    """
    A impressjs entry, control impressjs slide effects, actions and styles.
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        env = self.state.document.settings.env
        event = self.arguments[0]
        if len(self.arguments) == 2:
            contents = self.arguments[1]
        else:
            contents = '\n'.join(self.content)

        # Add feature specific implementation to here.

        if 'class' in self.options:
            node['classes'] += options['class']

        return [node]


def visit_impressjs_node(self, node):
    self.body.append(self.starttag(node, 'div'))
    self.body.append(node.rawsource)
    self.set_first_last(node)


def depart_impressjs_node(self, node=None):
    self.body.append('</script>\n')


def setup(app):
    app.add_node(impressjs_node, html=(visit_impressjs_node, depart_impressjs_node))

    app.add_directive('impressjs', Impressjs)
