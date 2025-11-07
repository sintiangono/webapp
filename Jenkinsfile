pipeline {
    agent any
    environment {
        DOCKERHUB = credentials('dockerhub')
        IMAGE = 'sintiangono/cc-webapp'
        FORCE_TAG = "${env.BUILD_NUMBER}"
    }
    stages {
        stage('Build') {
            steps {
                sh "docker build -t $IMAGE:$FORCE_TAG ."
            }
        }
        stage('Push') {
            steps {
                sh 'echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin'
                sh "docker push $IMAGE:$FORCE_TAG"
            }
        }
    }
    post {
        success {
            echo "IMAGE POUSSÉE : $IMAGE:$FORCE_TAG"
        }
    }
}
