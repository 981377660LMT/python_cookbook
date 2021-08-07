from posixpath import dirname
import sys
from os.path import join, dirname

foo_path = join(dirname(__file__), 'foo-package')
bar_path = join(dirname(__file__), 'bar-package')
sys.path.extend([foo_path, bar_path])

import spam.blah
import spam.grok
