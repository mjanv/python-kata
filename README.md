# Python Kata

*Python minimal code to run a [kata](https://en.wikipedia.org/wiki/Kata_(programming))*

### Install

```
virtualenv py3
source py3/bin/activate
pip install -r requirements.txt
```

### Run

```
pytest # Classic
ptw # Watch mode
pytest kata --cov-report xml:cov.xml --cov kata # Coverage support
ptw -- kata --cov-report xml:cov.xml --cov kata # Watch mode + Coverage support
```

### VSCode extensions
* [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters)
* [Python Test Explorer](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)