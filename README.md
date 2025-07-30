# Setup the workspace (CMD)
```bash
conda deactivate
```
```bash 
pip install uv
```
```bash 
uv init Workspace_Name_(Option)
```
```bash 
.venv/Scripts/activate
```
_to list python versions_
```bash 
uv python list
```
_to install specific python version_
```bash 
uv python install specific_python_version
```
_to create virtual env with specific python version_
```bash 
uv venv env --python specific_python_version
```

```bash 
uv add -r requirements.txt 
```
_to list the installed packages_
```bash 
uv pip list
```
_to see the previos commands you written_
```bash 
$ doskey/history
```


# To run the API
```
$ python main.py
```