## Haddock
Intellectual swearing for intellectual beards.

## Architecture
Haddock is based on a rock solid foundation. The various parts are described
below:

* `adjectives` is a list of strings
* `nouns` is a list of other strings

The actual moving parts are described below:

* `random_curse` is a function that returns some tokens that when combine
make up a somewhat absurd curse towards a singular thing.

## Examples
When run from the command line it will just print a random curse:

	> python .\haddock.py
	Haddock yells: raggle taggle bloodsucker!

Of course you can always just invoke the `random_curse` function but you 
need to `join` the tokens together. They are kept seperate so you can do
some kind of effects (like coloring) on them.

	curse = random__curse()
	print(' '.join(curse))

As an aside, it's also much easier to inspect and test the function (and 
play around with it) if you get the tokens and not a packed string.