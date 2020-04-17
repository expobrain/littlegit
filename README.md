# Littlegit

A very little Python wrapper around Git CLI.

Littlegit doesn't need any external dependency except for the [Git](https://git-scm.com/) binary to be installed in your system.

All the current, past and future commands and options of Git are fully supported.

## Installation

Install Littlegit with `pip`:

```
pip install littlegit
```

## Usage

To use Littlegit is very simple, it follows a very simple rule to map Git's commands to Littlegit's API:

- every Git command is a method
- every argument is a method's argument
- every option is a method's keywords

Lets explain this with an example of initialising a local repository, adding a file and commiting:

```python
from pathlib import Path

from littlegit import Git

repo = Git(Path("/my/local/repo"))
repo.init()  # git init /my/local/repo

open("myfile", "w").close()

repo.add("myfile")  # git add myfile
repo.commit(message="this is my first commit")  # git commit --message "this is my first commit"
repo.remote("add", "origin", "<my_remote_repo>")  # git remote add origin <my_remote_repo>
repo.push("origin", "master")  # git push origin master
print(repo.log(_1=True))  # get only the last log message
```

All the methods return the output if the Git command:

```python
output = repo.branch(remote=True)  # git branch --remote
print(output)
origin/HEAD -> origin/master
origin/master
```

## Tests

To run the unit tests install the development dependencies and then run [PyTest](https://pytest.org/):

```
pip install -r requirements_dev.txt
pytest tests.py
```
