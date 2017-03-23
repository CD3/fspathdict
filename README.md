# Path Dectionary

A simple class to allow filesystem-style path access, including support for walking "up" the dict with '..'.

Example:

```python
config = pdict()
config.update( { 'desc' : "example config"
               , 'time' : { 'N' : 50
                          , 'dt' : 0.01 }
               , 'grid' : { 'x' : { 'min' : 0
                                  , 'max' : 0.5
                                  , 'N' : 100 }
                          , 'y' : { 'min' : 1
                                  , 'max' : 1.5
                                  , 'N' : 200 }
                          }
               } )

# elements are accessed in the same was as a dict.
assert config['desc'] == "example config"
# sub-elements can also be accessed the same way.
assert config['grid']['x']['max'] == 0.5
# but they can also be accessed using a path.
assert config['grid/x/max'] == 0.5

# get a sub-element in the tree.
x = config['grid/x']

# again, elements of grid/x are accessed as normal.
assert x['max'] == 0.5
# but we can also access elements that are not in this branch.
assert x['../y/max'] == 1.5
# or reference elements from the root of the tree.
assert x['/time/N'] == 50
```
