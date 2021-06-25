# Docker 101  

<small>by ashikshezan</small>

## a. Installing docker

Installing Docker in Manjaro:

```bash
sudo pacman -Syu docker
```

Check the version 

```bash
docker version
```

To start the the **docker** engine,

```bash
sudo systemctl start docker
```

or

```bash
sudo systemctl enable --now docker
```

To give the user permission to run docker or to remove the `sudo` statement

```bash
sudo gpasswd -a $USER docker
```

## b. Installing docker-compose

Docker compose can be install easily with `pip` 

```bash
pip install docker-compose
```



## Example Airflow Project Using Docker

1. Create a new project directory and `cd` to that

   ```bash
   mkdir airflow_project
   cd airflow_project
   ```

2. Download the `docker-compose.yaml` to set all the configurations

   ```bash
   curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.1.0/docker-compose.yaml'
   ```

3. Make 3 new directory and set some environment variables

   ```bash
   mkdir ./dags ./logs ./plugins
   echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
   ```

4. On **all operating systems**, you need to run database migrations and create the first user account. To do it, run

   ```bash
   docker-compose up airflow-init
   ```

5. Now you can start all services

   ```bash
   docker-compose up
   ```

6. To interact with the airflow container from the terminal need to do this configuration

   ```bash
   curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.1.0/airflow.sh'
   chmod +x airflow.sh
   
   ```

7. Now for python or for bash terminal 

   ```bash
   ./airflow.sh bash
   ```

   or

   ```bash
   ./airflow.sh python
   ```

   or for info

   ```bash
   ./airflow.sh info
   ```

   

