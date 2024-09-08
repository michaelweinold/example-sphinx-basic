# Sphinx Debugging

For debugging, one could:

1. Copy `brightway2-data` into the root directory of the project.
2. Run the following command from the root directory of the project:

```bash
sphinx-build docs _build/html --builder=singlehtml --jobs=auto --write-all; open _build/html/index.html
```

3. Tinker around with the `bw2data/parameters.py` file until the build succeeds.