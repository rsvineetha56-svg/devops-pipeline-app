pipeline {
    agent any
    environment {
        IMAGE = 'devops-demo-app'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'docker build --target test -t $IMAGE-test .'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker compose up -d --build --remove-orphans'
            }
        }
        stage('Smoke Test') {
            steps {
                sh '''
                    sleep 10
                    curl -fsS http://localhost:5000/health
                    curl -fsS http://localhost:5000/
                '''
            }
        }
        stage('Monitoring Check') {
            steps {
                sh '''
                    sleep 20
                    curl -fsS http://localhost:9090/-/ready
                    curl -fsS http://localhost:9090/api/v1/targets | grep -q '"health":"up"'
                '''
            }
        }
    }
    post {
        success { echo 'Pipeline succeeded: app deployed and monitored.' }
        failure { echo 'Pipeline failed: check the stage that turned red.' }
    }
}
