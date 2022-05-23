pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh "venv/bin/pip install -r src/app/requirements.txt"
            }
        }
        stage('Test') { 
            steps {
                sh "venv/bin/python3 -m pytest -p no:cacheprovider"
            }
        }
        stage('Deploy') { 
            steps {
                sh 'ssh -o StrictHostKeyChecking=no dima@171.25.204.100 \
                    "cd sharpe_explorer/backend/ \
                    && git pull origin master \
                    && cd .. \
                    && docker-compose up -d"'
            }
        }
    }
}