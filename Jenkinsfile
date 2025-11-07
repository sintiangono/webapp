pipeline {
    agent any
    environment {
        DOCKERHUB = credentials('dockerhub')
        IMAGE = 'sintiangono/cc-webapp'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t $IMAGE:${BUILD_NUMBER} ."
            }
        }
        stage('Push') {
            steps {
                sh 'echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin'
                sh "docker push $IMAGE:${BUILD_NUMBER}"
            }
        }
    }
    post {
        success {
            echo "Image pushed: $IMAGE:${BUILD_NUMBER}"
        }
        failure {
            echo "Build failed!"
        }
    }
}	
