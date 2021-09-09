+++
title = "hash a nested python dictionary"
description = ""
date = "2021-03-16"
heading= true
+++

I came upon a Python situation recently where I had to hash a dictionary of arbitary depth, where:

1. all keys are strings
2. all values are either strings, numbers (numpy or native python ints/floats), basic iterables (non-object dtype numpy `ndarrays`, numerical pandas `Series`, or native python `list`s or `tuple`s of python native numbers/strings), OR...
3. ...values are themselves dictionaries subject to these 3 rules. 

For example:

```
some_dictionary = {

	"a": 12,
	"b": "some_string",
	"c": {
		"q": np.ndarray([1,2,3...]),
		"some_key": pd.Series([19.283, 20.873....]),
		"k": 11,
		"a": {
			"nested_key": [8, 9, 11],
			"other nested key": (11, 15),
			"c": "eleven",
			"d" : { 
				# of arbitrary depth
				...
			}
		}
	}
	"d": np.ndarray([0.001, 0.002, 0.003...]),
	"something": np.int64(40000),
	...
	# of arbitrary length
}
```

How would we possibly hash this?


## A solution

If you're feeling intimidated, then you know how I felt when there was no answer to be found on StackOverflow or seemingly _anywhere_ in the Googlesphere. So, in the spirit of a frantic coding interview, I wrote a brief (? maybe?) solution that works (pretty well? as far as I know?).

```
import hashlib
import json

import numpy as np
import pandas as pd


# Collapse the dictionary to a single representation
def immutify_dictionary(d):
    d_new = {}
    for k, v in d.items():
	
	# convert to python native immutables
        if isinstance(v, (np.ndarray, pd.Series)):
            d_new[k] = tuple(v.tolist())

	# immutify any lists
        elif isinstance(v, list):
            d_new[k] = tuple(v)

	# recursion if nested
        elif isinstance(v, dict):
            d_new[k] = immutify_dictionary(v)

	# ensure numpy "primitives" are casted to json-friendly python natives
        else:
            # convert numpy types to native
            if hasattr(v, "dtype"):
                d_new[k] = v.item()
            else:
                d_new[k] = v
    
    return dict(sorted(d_new.items(), key=lambda item: item[0]))

# Make a json string from the sorted dictionary
# then hash that string
def hash_dictionary(d):
    d_hashable = immutify_dictionary(d)
    s_hashable = json.dumps(d_hashable).encode("utf-8")
    m = hashlib.sha256(s_hashable).hexdigest()
    return m
```


Here's an example:

```
d = {
	"q": [1, 2, 3], 
	"b": {
		"c": "12", 
		"d": 15, 
		"e": np.asarray([4, 5, 6]),
                "f": {
			"z": 12, 
			"a": [7, 8]
		}
	}, 
	"c": np.int64(400)
}
```

```
>>> hash_dictionary(d)

'e68f1472030c1dbba09fda5eca116c9e7d5ae37e4742d619102b63972fdf9e50'
```

Note if we permute the keys (Python 3.6+ dictionaries are insertion-sorted, but we are considering dictionaries unsorted as they can be permuted while holding the same data) we obtain the same result:

```
d_permuted = {
        "b": {
                "c": "12", 
                "f": {
                        "a": [7, 8],
                        "z": 12, 
                },
                "e": np.asarray([4, 5, 6]),
                "d": 15, 
        }, 
        "c": np.int64(400),
        "q": [1, 2, 3], 
}
```

```
>>> hash_dictionary(d_permuted)

'e68f1472030c1dbba09fda5eca116c9e7d5ae37e4742d619102b63972fdf9e50'
```

But if we change any of the keys or the values, we get a different hash:

```
d_new_value = {
        "b": {
                "c": "12",
                "f": {
                        "a": [7, 8],
                        "z": 12,
                },
                "e": np.asarray([4, 5, 6]),
                "d": 15,
        },

	# changed this value
        "c": np.int64(399),
        "q": [1, 2, 3],
}
```

```
>>> hash_dictionary(d_new_value)

'2e3756de5565262aba8f0f888d2938cde93e5b6bc4735b730f673a798a9d72d5'
```



If you find a more concise/performant solution, or find an edge case where this does not work, please email me! This solution relies on making a copy of the dictionary which is not efficient in terms of memory, so there is likely a better way to do inplace or without sorting.


## Walkthrough 


<br> 

#### Mutability 

In Python, dictionaries are unhashable because they are _mutable_, meaning they can be changed. So we need a way to get an immutable version of (or 'immutify') a dictionary subject to the constraints above. Everything inside the dictionary must also be immutable; for example, Python `list`s are not hashable because they are mutable.


If you are dealing with the most basic case, where the dictionary is flat:

```
{
	key_1: value_1,
	key_2: value_2,
	key_3: value_3,
}
```


Python's builtin `frozenset` function makes it trivial to immutify this dictionary. You can think of what `frozenset` does as similar to creating an immutable `set` of `tuple`s, which together is immutable and therefore hashable. Provided your values are themselves hashable (e.g., native Python numbers, strings, tuples, etc.) `frozenset` immediately solves your problem.


However, if we make the dictionary a bit more complicated and include mutable datatypes as values, we will need to immutify them before creating a frozenset:


```
{
	key 1: [item1, item2, item3],
	key 2: (item4, item5),
	key 3: value_3,
	key 4: np.ndarray([1,2,3])
}
```


The lists can be changed to `tuple`s with the `tuple()` function; the builtin `ndarray.tolist()` will take care of changing numpy and pandas objects to native lists, which then can be cast to immutable tuples. 

For values which are themselves numpy primitive data types (e.g., `int64`), these should be cast to python natives.

---

#### Recursion

We add yet another layer of complexity when we consider that any dictionary value can itself be another dictionary. The only way to deal with this is recursion - or _dynamic programming_ if we're feeling particularly fancy.

The pseudocode for dealing with this problem is:

```
function immutify_dictionary(d)
	for key, value in d
		if type(value) = dictionary
			immutify_dictionary(value))
		else:
			immutify_iterable_or_primitive(value)
```

The algorithm runs over values until it either runs into a "stop point" (array or primitive) or recursively continues by finding a dictionary value.

---


#### Regular `hash` doesn't cut it

Provided we can now get each part of our dictionary into an immutable form, we still face a problem. The builtin python hash, which can natively hash python objects, does not give reliable digests because it is seeded with a random number from the system as a source of entropy. Instead, we need to use the `hashlib` module (specifically, SHA256).

However, the `hashlib` algorithms require strings as input, **not any immutable python object**. 

So as opposed to using `hash` on a `frozenset`, where ordering does not matter, we must (1) order the dictionary deterministically and then (2) convert the dictionary to a string. If dictionary A and dictionary B have the same keys and same values but are string-ified with different orderings, they will have different hashes! Essentially...


> Essentially, if two dictionaries have the same information contained in them, **they must produce the same dictionary string** and therefore **the same hash**. 


At first it may seem like our previous work immutifying the dictionary is wasted, since we'll be immutifying by just converting our dictionaries to a big string. This is not true. **Since different formats of the same data must be represented identically, different formats of arrays or numbers must collapse to the same string.** In other words, running the code for immutification will collapse the various numpy/pandas/native arrays into the same tuples and the various primitive numerical types to the native python types. Our work was not wasted!


This is where the final line of `immutify_dictionary` comes in:
```
return dict(sorted(d_new.items(), key=lambda item: item[0]))
```


This line simply re-sorts the dictionary by the keys, producing an insertion-sorted dictionary as output. 


Next, this sorted, deterministically collapsed dictionary can truly become immutable:

```
d_hashable = immutify_dictionary(d)
s_hashable = json.dumps(d_hashable).encode("utf-8")
```


The `s_hashable` here is just itself a very long "hash" of the input dictionary. The same information, **regardless of insertion order or  array/primitive format, collapses to the same string**.

---

#### The final step 

Much shorter than the string representation of the dictionary is the hexdigest of the SHA256 hash of that string. That is where `hashlib` finally comes in:


```
   m = hashlib.sha256(s_hashable).hexdigest()
```

The output is the 256-bit, or 64-hex character digest of our dictionary.




