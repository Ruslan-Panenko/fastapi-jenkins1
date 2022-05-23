pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh "/var/lib/jenkins/workspace/sharpe/venv/bin/pip install -r src/app/requirements.txt"
            }
        }
        stage('Test') { 
            steps {
                sh "tests"
            }
        }
        stage('Deploy') { 
            steps {
                sh "echo deploy"
            }
        }
    }
}