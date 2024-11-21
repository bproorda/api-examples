python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

pip install fastapi pytest httpx

why use python virtual environment? 
The command "python -m venv venv" followed by "source venv/bin/activate" is used to create and activate a virtual environment in Python. Here's why this approach is beneficial:

## Creating a Virtual Environment

"python -m venv venv" creates a new virtual environment:

1. It isolates project dependencies from the system-wide Python installation[1].
2. It allows you to work on multiple projects with different package versions without conflicts[2].
3. It creates a clean, reproducible environment for your project[1].

## Activating the Virtual Environment

"source venv/bin/activate" activates the virtual environment:

1. It modifies your shell's PATH to prioritize the virtual environment's Python interpreter[1].
2. It ensures that pip installs packages into the virtual environment, not the system-wide Python[1].
3. It isolates your project's package installations from other projects[2].

## Benefits

Using virtual environments offers several advantages:

1. **Dependency isolation**: Each project can have its own set of dependencies without interfering with others[2].
2. **Version control**: You can specify exact versions of packages for your project, ensuring consistency across different development environments[1].
3. **Clean testing environment**: It provides a fresh Python environment for testing your code without system-wide package interference[2].
4. **Easy replication**: You can easily share your project's environment specifications with others, ensuring they can recreate the same setup[1].

By using "python -m venv venv" to create and "source venv/bin/activate" to activate a virtual environment, you're following best practices for Python development, ensuring a clean, isolated, and reproducible environment for your projects[1][2].

Citations:
[1] https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
[2] https://www.geeksforgeeks.org/python-virtual-environment/
[3] https://code.visualstudio.com/docs/python/environments
[4] https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
[5] https://docs.python.org/ja/3.13/library/venv.html
[6] https://realpython.com/python-virtual-environments-a-primer/
[7] https://www.youtube.com/watch?v=7Qi10Ba1eL8
[8] https://it.engineering.oregonstate.edu/setting-virtual-environments-python