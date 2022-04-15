Trying to figure out why mypy isn't happy with this.

Check this out, cd to the directory, and run `mypy test.py`, and it returns:

```
error: Module "tdvutil" has no attribute "ppretty"
```

Best I can tell, I'm following relatively normal patterns here. I've tried
variations on this theme without better results. What am I doing wrong?
Basically I just want to be able to do `from tdvutil import ppretty`, but
have the actual implementation for the ppretty function be in a different
file than `tdvutil/__init__.py`.

From my understanding, the combination of `from ._ppretty import ppretty`
and the `__all__` variable that includes `ppretty` should make this happen.

The code itself runs and does the right thing.

What am I missing?
