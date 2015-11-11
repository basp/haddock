## Haddock
Intellectual swearing for intellectual beards. Haddock tries to make swearing 
fun again. For too long we have been stuck in the same sequence of swear words
over and over again. 

Haddock is here to remind you of some awesome swear words
and you can look smart in the process as well by using words that are either
extremely obscure or just plain made up.

Be prepared to amaze your peers with some *dunderheaded* *misguided* swearing.

## Architecture
Haddock is based on a rock solid foundation. The various parts are described
below:

* `adjectives` is a list of strings
* `nouns` is a list of other strings

The actual moving parts are described below:

* `random_curse` is a function that returns some tokens that when combined
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

## TODO
* Create good database of vocab.
* Over-engineer
* Publish npm and various other formats
* Create community
* Create startup
* Make web API
* Get rich