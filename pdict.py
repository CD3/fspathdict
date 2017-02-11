import collections

class pdict(collections.MutableMapping):
  """A dictionary that allows nested element access using key paths."""

  def __init__(self,*args,**kwargs):
    self.parent = None
    self.store = dict()
    self.update(dict(*args, **kwargs))  # use the free update to set keys
    self.recursive_convert()

    self.delimiter = '/'
    self.pup = '..'
    self.phere  = '.'

  def __getitem__(self, key):
    # split key into path elements
    key = str(key)
    toks = key.split(self.delimiter,1)
    head = toks[0]
    tail = None if len(toks) < 2 else toks[1]

    if head == self.pup:
      # first path element references parent
      return self.parent if tail is None else self.parent[tail]
    elif head == self.phere:
      # first path element references self
      return self if tail is None else self[tail]
    else:
      # first path element references key or index
      if isinstance(self.store,list):
        # if internal storage is a list, convert head to an int
        head = int(head)
      return self.store[head] if tail is None else self.store[head][tail]

  def __setitem__(self, key, value):

    # if value is a dict, convert it to a pdict
    if isinstance(value,(dict,list)):
      newvalue = pdict()
      newvalue.store = value
      value = newvalue
    
    if isinstance(value,pdict):
      value.parent = self
      value.recursive_convert()

    self.store[key] = value

  def recursive_convert(self):
    # recursively convert any nested dict's to pdict's
    for k in (self.store if isinstance(self.store,dict) else [i for i,v in enumerate(self.store)]):
      if isinstance(self[k], (dict,list)):
        self[k] = self.store[k]

  def __delitem__(self, key):
    del self.store[key]

  def __iter__(self):
    return iter(self.store)

  def __len__(self):
    return len(self.store)
