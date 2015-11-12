import re

#
# ident = [a-zA-Z_][a-zA-Z0-9_]*
# style = <renderer>(obj[.attr])

# We might think we have two kinds of renderers but we do not.
# They are exactly the same if we consider one a limited version
# of the other.
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

		
	 