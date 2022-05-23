pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh "source venv/bin/activate && pip install -r src/app/requirements.txt"
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