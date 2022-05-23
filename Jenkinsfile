pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                bash "source venv/bin/activate && pip install -r src/app/requirements.txt"
            }
        }
        stage('Test') { 
            steps {
                bash "tests"
            }
        }
        stage('Deploy') { 
            steps {
                sh "echo deploy"
            }
        }
    }
}