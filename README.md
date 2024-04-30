# PyPiRepoTemplate
Template repo for making a pypi package


# Repo setup checklist
- [ ] Set up venv and install packages in `dev-requirements.txt`
- [ ] Run the generate script `00_RUN_ME_TO_GENERATE_generate_repo_content.py`
- [ ] Edit read the docs link and update docs
- [ ] Tests and Examples
- [ ] Initial run and publish of the package

# USER GUIDE -> \*\*Read-The-Docs!\*\* [Link](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## DEVELOPMENT - Publishing a new version of this package
- Update the version number in `setup.py` try to use [sem ver](https://semver.org/) as a guide for which number to bump
- Run `build_docs_script.py` to regenerate the autogen docs
- Run `build_package_script.py` to build a new version of the package
- Make sure your `dist/` folder contains only the new version (could fail if not!)
- Run `publish_package.py` to upload the contents to the dist/ folder to pypi
