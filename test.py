# -*- coding: utf-8 -*-
#
# Copyright © 2019 Stephan Seitz <stephan.seitz@fau.de>
#
# Distributed under terms of the GPLv3 license.

"""

"""

from tree_sitter import Language, Parser
from queue import SimpleQueue


Language.build_library(
  # Store the library in the `build` directory
  'build/my-languages.so',

  # Include one or more languages
  [
    'tree-sitter-cpp',
  ]
)

CPP_LANGUAGE = Language('build/my-languages.so', 'cpp')
parser = Parser()
parser.set_language(CPP_LANGUAGE)

tree = parser.parse(bytes("""
#include <iostream>
#include <cstdlib>

auto main( int argc, char** argv ) -> int
{
    std::cout << "Hello world!" << std::endl;
    
    return EXIT_SUCCESS;
}
""", "utf8"))


# Breadth first
queue = SimpleQueue()
queue.put(tree.root_node)

while not queue.empty():
    node = queue.get()
    print(node.type)
    for child in node.children:
      queue.put(child)
print("\n")
print("\n")
# Depth first
stack = [tree.root_node]

while stack:
    node = stack.pop()
    print(node.type)
    stack.extend( reversed(node.children))

