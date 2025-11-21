pipeline {
    agent {
        docker {
            image 'python:3.13'
            args '-u root'
            reuseNode true
        }
    }

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
        AWS_DEFAULT_REGION = 'ap-south-1'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install -r requirements.txt
                pip install awscli aws-sam-cli
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                export PYTHONPATH=$PWD
                pytest
                '''
            }
        }

        stage('Build SAM Package') {
            steps {
                sh '''
                rm -rf .aws-sam
                sam build
                '''
            }
        }

        stage('Deploy to AWS') {
            steps {
                sh '''
                sam deploy --no-confirm-changeset --config-file samconfig.toml
                '''
            }
        }
    }

    post {
        always {
            echo "CI/CD finished!"
        }
    }
}
