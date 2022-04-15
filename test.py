#!/usr/bin/env python3

# this line gives this:
#   "error: Module "tdvutil" has no attribute "ppretty"
# ...why?
from tdvutil import ppretty as ppretty



# and then some code to show it actually works
teststruct = {
    "something": "something",
    "somethingelse": {
        "somethingelse1": "somethingelse1",
        "somethingelse2": "somethingelse2",
    }
}

print("test output:\n" + ppretty(teststruct))
