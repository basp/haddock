from collections import namedtuple
import re

#
# ident = [a-zA-Z_][a-zA-Z0-9_]*
# style = <renderer>(obj[.attr])
#

# Globally there are a few main things a renderer should do:
#
# 1. Escape if necessary
# 2. Identify the areas that need to be rendered
# 3. Parse the rendering information in those areas
# 4. Replace the rendering information and markup with the output

#
# Could do a rendering-chain where we have a next renderer 
# instead of just an array of render functions.

#
# * We have push tags and pop tags.
# * A push tag pushes a style onto the rendering stack
# * A pop tag pops a style from the rendering stack
# * A renderer is responsible for looking up a particular style
# * Of course it can delegate this task how it desires
# * A client should be able to clearle control and specify the rendering pipeline
# * There's a single reserved style _default
# * Every renderer should support this style
# * There's probably also a reserved renderer %(<obj>[.<attr>])

#
# Instruction format: <style(obj[.attr] /> or it can also be a <style(obj[.attr]> to </antyhing_goes_here>
# The first one will just execute the render function, replace the rendering tag and pop the stack.
# The second one will execute the render function and will pop the stack when it encounters the end tag.

