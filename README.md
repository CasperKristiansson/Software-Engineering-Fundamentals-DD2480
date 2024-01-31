# DD2480G24

### Testing

The unit testing is based on the Python built in `unittest` framework (https://docs.python.org/3/library/unittest.html)

To run all tests in a file:
- `python -m unittest <path to testfile>`

## CI/CD

We are utilizing GitHub Actions for CI/CD. The workflow is defined in `.github/workflows/`. We have three different kinds of GitHub Actions workflows:

- `generate-documentation.yml` - This workflow is triggered when a merge to the `main` branch is made. It generates the documentation alongside a PDF and creates a new release.. The documentation is added to the release along with with a text describing the changes made since the last release.
- `python-tests.yml` - This workflow is triggered on all `pull requests`. It runs the unit tests in the directory `tests/`.
- `generate-website.yml` - This workflow is triggered after the workflow `generate-documentation.yml` is completed. It than generates the documentation alongside a HTML webpage. The webpage is than pushed to github pages.

## Documentation
Adding New Modules to Sphinx Documentation
To include new modules in the Sphinx documentation, use the following command:

```bash
sphinx-apidoc -o docs/source/ src/
```

This command generates reStructuredText files in the docs/source/ directory, based on the modules found in the src/ directory.

### Building the Documentation as an HTML Page

To build the documentation into HTML format, follow these steps depending on your operating system:

**For Windows:**

Navigate to the docs directory:

```bash
cd docs
```

Then, run the make batch file:

```bash
.\make.bat html
```

**For Linux:**

Navigate to the docs directory:

```bash
cd docs
```

Then, use the make command:

```bash
make html
```

This process will compile the Sphinx documentation into HTML pages, which can be found in the docs/build/html directory.

### Generating Documentation as a PDF

To create a PDF version of your Sphinx documentation, we use the following commands:

Navigate to the docs directory:

```bash
cd docs
```

Then, run the following command:

```bash
sphinx-build -b pdf source build/pdf
```

This command instructs Sphinx to build the documentation in PDF format.
