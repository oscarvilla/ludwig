# Ludwig basic environment
This is an experimet tying to automate the creation on an environment for experiment with Ludwig on Python 3.8

Throught a Make file we:
- Install venv for Python 3.8
- Create an venv based on Python  3.8
- Activate the venv
- Update pip and install requirements

## Other things you need to be sure:
Even if it sounds obvious, yo need to be sure that:
- You activate the environment on the shell `source ./env/bin/activate`
- You select the environment as your Python Interpreter.

## Next:
So, now you can run the demo.py script and inspect the results.

Create a virtualenv
```python3 -m venv ~/.github-actions-demo```

Source it
```source ~/.github-actions-demo/bin/activate```

### The repo is a scaffolding with multiple options

#### requirements.txt

You have here multiple file requirements, in case you have multiple instances in which you like to deploy your dev environment

#### *.yml

There are multiple pipelines for testing, formating and installations that run on Github actions
