# Setup the workspace (CMD)
```
conda deactivate
```
``` 
pip install uv
```
``` 
uv init Workspace_Name_(Option)
```
``` 
.venv/Scripts/activate
```
_to list python versions_
``` 
uv python list
```
_to install specific python version_
``` 
uv python install specific_python_version
```
_to create virtual env with specific python version_
``` 
uv venv env --python specific_python_version
```

``` 
uv add -r requirements.txt 
```
_to list the installed packages_
``` 
uv pip list
```
_to see the previos commands you written_
``` 
doskey/history
```


# To run the API
```
python main.py
```

# Deploy the model on AWS cloud with CD aproach
1) Create an IAM user with the following policies: `AmazonEC2FullAccess` - `AmazonEC2ContainerRegistryFullAccess`.
2) Go to the `Security credentials` tap in the created user in the previos step and create _access key_ for it, then, download the .csv file.
3) Create a repository on Amazon ECR, copy its URI (i.e. 962265167812.dkr.ecr.us-east-1.amazonaws.com/your-repo-name) and save it.
4) Launch EC2 instance with ubuntu VM, connect to it and run the following commands:
```
sudo apt-get update -y
```
```
sudo apt-get upgrade
```
Install Docker Engine
```
curl -fsSL https://get.docker.com -o get-docker.sh
```
```
sudo sh get-docker.sh
```
```
sudo usermod -aG docker ubuntu
```
```
newgrp docker
```
5) Go to your Github repo, `Settings -> Actions -> Runners`, choose `New self-hosted runner`, then `Linux`, and finally execute all the commands in the EC2 instance VM.
6) In the same `Settings` tap in your repo, go to `Secrets and Variables`, choose `Actions` and create `New repository secrets` with the following secrets:
    * `AWS_ACCESS_KEY_ID` : from the .csv file you downloaded in step 2.
    * `AWS_SECRET_ACCESS_KEY` : also from the same .csv file.
    * `AWS_REGION` : _us-east-1_ for me.
    * `ECR_REPOSITORY_NAME` : your ECR repo name you created in step 3.
    * `ECR_REPOSITORY_URI` : the URI you copied in step 3.
    * `PINECONE_API_KEY` : from .env file in your workspace.
    * `GROQ_API_KEY` : from .env file also.