pipeline {
    agent any
    environment {
        DOCKERHUB = credentials('dockerhub')
        IMAGE = 'sintiangono/cc-webapp'
        TAG = "${env.BUILD_NUMBER}"
    }
    stages {
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin'
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t $IMAGE:$TAG ."
            }
        }
        stage('Push') {
            steps {
                sh "docker push $IMAGE:$TAG"
            }
        }
    }
    post {
        success {
            echo "POUSSÉ : $IMAGE:$TAG"
        }
        always {
            sh 'docker logout'
        }
    }
}
