# lazyprop
Python decorator for easy lazy loading class properties

[![CircleCI](https://circleci.com/gh/dbjohnson/lazyprop.svg?style=shield)](https://circleci.com/gh/dbjohnson/lazyprop)[![![PyPi](https://img.shields.io/pypi/v/lazyprop.svg)](https://pypi.python.org/pypi/lazyprop)
[![Code Climate](https://codeclimate.com/github/dbjohnson/lazyprop/badges/gpa.svg)](https://codeclimate.com/github/dbjohnson/lazyprop)
[License](https://img.shields.io/github/license/dbjohnson/lazyprop.svg)]()

## Installation
```pip install lazyprop```

## Usage
Decorate any class method to memoize / cache object properties.

```python
from lazyprop import lazyprop

class Foo(object):
    def __init__(self):
        self.load_count = 0

    @lazyprop
    def lazy(self):
        self.load_count += 1
        
        
>> f = Foo()
>> f.lazy
>> f.lazy  # second access should use cached result
>> print(f.load_count)
1
