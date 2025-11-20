pipeline {
    agent any

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

        stage('Install Dependencies') {
            steps {
                bat '''
                pip install -r requirements.txt
                pip install awscli aws-sam-cli
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                set PYTHONPATH=%cd%
                pytest
                '''
            }
        }

        stage('Build SAM Package') {
            steps {
                bat '''
                sam build
                '''
            }
        }

        stage('Deploy to AWS') {
            steps {
                bat '''
                sam deploy --no-confirm-changeset --stack-name calculator-stack --capabilities CAPABILITY_IAM
                '''
            }
        }
    }

    post {
        always {
            echo "CI/CD pipeline finished!"
        }
    }
}
