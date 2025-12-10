pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred')
        EC2_SSH_KEY = credentials('ec2-ssh-key')
        IMAGE_NAME = "merontemesgen/women-techsters-app:latest"
        EC2_USER = "ubuntu"
        EC2_IP = "YOUR_EC2_IP"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'GROUP-A', url: 'https://github.com/merontemesgen/Women_Tech_practise.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME} .
                """
            }
        }

        stage('Login to Docker Hub') {
            steps {
                sh """
                echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin
                """
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh """
                docker push ${IMAGE_NAME}
                """
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh """
                ssh -o StrictHostKeyChecking=no -i ${EC2_SSH_KEY} ${EC2_USER}@${EC2_IP} '
                    sudo docker pull ${IMAGE_NAME} &&
                    sudo docker stop app || true &&
                    sudo docker rm app || true &&
                    sudo docker run -d --name app -p 5000:5000 ${IMAGE_NAME}
                '
                """
            }
        }
    }
}
