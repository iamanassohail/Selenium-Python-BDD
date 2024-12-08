pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'quickleaen'
        CONTAINER_NAME = 'dockerapp'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from your version control system
                git 'https://your-repo-url.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Create Docker Container') {
            steps {
                script {
                    // Create Docker container
                    sh 'docker create --name ${CONTAINER_NAME} -p 8080:80 ${DOCKER_IMAGE}'
                }
            }
        }

        stage('Start Docker Container') {
            steps {
                script {
                    // Start Docker container
                    sh 'docker start ${CONTAINER_NAME}'
                }
            }
        }

        stage('Stop Docker Container') {
            steps {
                script {
                    // Stop Docker container
                    sh 'docker stop ${CONTAINER_NAME}'
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up Docker containers
                sh 'docker rm -f ${CONTAINER_NAME} || true'
                // Optionally, remove Docker image
                // sh 'docker rmi ${DOCKER_IMAGE} || true'
            }
        }
    }
}
