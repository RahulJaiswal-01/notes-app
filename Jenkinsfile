pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t notes-app .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker rm -f notes-app-container || true'
                sh 'docker run -d --name notes-app-container -p 5000:5000 notes-app'
            }
        }
        stage('Deploy to K3s') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
