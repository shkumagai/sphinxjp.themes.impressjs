# -*- coding: utf-8 -*-

__docformat__ = 'reStrructuredText'

from docutils.parsers.rst import directives
from docutils.parsers.rst.roles import set_classes
from docutils import nodes
from sphinx.util.compat import Directive


class impressjs(nodes.General, nodes.Element): pass


class Impressjs(Directive):
    """
    A impressjs entry, control impressjs slide effects, actions and styles.
    """
    has_content = True
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True

    option_spec = {'data-x': int,
                   'data-y': int,
                   'data-z': int,
                   'data-rotate-x': int,
                   'data-rotate-y': int,
                   'data-rotate': int,
                   'data-scale-x': directives.length_or_unitless,
                   'data-scale-y': directives.length_or_unitless,
                   'data-scale': directives.length_or_unitless,
                   'id':int,
                   'class': directives.class_option ,
    }

    node_class = impressjs

    def run(self):
        """ build impressjs node """
        set_classes(self.options)
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = self.node_class(text, **self.options)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        if self.arguments[0]:
            node['ids'] += [self.arguments[0]]
        if 'class' in self.options:
            node['classes'].append(options['class'])

        return [node]


def visit_impressjs(self, node):
    """  """
    atts = {'class': 'step'}
        
    if 'data-x' in node:
        atts['data-x'] = node['data-x']
    if 'data-y' in node:
        atts['data-y'] = node['data-y']
    if 'data-z' in node:
        atts['data-z'] = node['data-z']
    if 'data-rotate-x' in node:
        atts['data-rotate-x'] = node['data-rotate-x']
    if 'data-rotate-y' in node:
        atts['data-rotate-y'] = node['data-rotate-y']
    if 'data-rotate' in node:
        atts['data-rotate'] = node['data-rotate']
    if 'data-scale-x' in node:
        atts['data-scale-x'] = node['data-scale-x']
    if 'data-scale-y' in node:
        atts['data-scale-y'] = node['data-scale-y']
    if 'data-scale' in node:
        atts['data-scale'] = node['data-scale']
    # if 'id' in node:
    #     atts['id'] = node['id']

    self.body.append(self.starttag(node, 'div', **atts))
    self.set_first_last(node)


def depart_impressjs(self, node=None):
    self.body.append('</div>\n')


def setup(app):
    app.add_node(impressjs,
                 html=(visit_impressjs, depart_impressjs))
    app.add_directive('impressjs', Impressjs)
