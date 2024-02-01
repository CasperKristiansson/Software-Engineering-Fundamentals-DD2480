# DD2480G24

### DECIDE
This project creates an implementation for the DECIDE program specified in the file
`specification.pdf` contained within the `docs` folder

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

## Methodology Self-Assessment
Currently the team lies somewhere inbetween "In Use" and "In Place". The first
item, "Principles Established" was covered in the first meeting held by group,
when agreeing on the code-of-conduct. During that meeting, the team decided
general approach necessary as well as what kind of tools would be necessary
and used. Later, a second meeting was held to discuss the specifics (such as
exact tools and versions, roles, responsibilities, and other specifics) that
established the clearance for "Foundation Established" as well as some first
tasks to get the project started. During the continuation of the project, the
team has evolved the usage of the tools and practices to taking a place in
the "In Place" state. To move further into "In Place" and in the end get to
"Working Well", the team simply needs more practice with the methodologies,
tools, and practices to make them second-nature rather than an attached task
for each moment in the project.

## Contributions

**Andreas**
- Main repo admin (issues, reviewing, labeling, etc)
- Summarised Self-Assessment into [README](#methodology-self-assessment)
- LIC 4, 5, 8

**Martin**
- Test suite responsible (create foundation for testing framework and project skeleton, review tests in pull requests)
- LIC 6, 9, 12
- Creation of the Preliminary Unlocking Matrix (PUM)

**Adam**
- Setup discord and git repo
- Discord webhooks integration
- LIC 0, 1, 2, 13

**Victor**
- Set up code skeleton for cmv, parser, pum, fuv, decide files
- LIC 3, 7, 11 with tests
- Parser with tests
- FUV with tests
- Decide with tests along with **Martin** and **Adam**

**Casper**
- Configured Sphinx to automatically generate documentation (with theme). This includes both a PDF and HTML version of the documentation.
- Setup GitHub Actions to:
    - Run python tests on pull requests
    - Generate documentation on merge to main
    - Generate website on merge to main
- LIC 10, 13 (co-authored), 14
