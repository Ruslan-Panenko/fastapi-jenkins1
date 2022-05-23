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
                sh "venv/bin/python3 -m pytest"
            }
        }
        stage('Deploy') { 
            steps {
                sh "echo deploy"
            }
        }
    }
}