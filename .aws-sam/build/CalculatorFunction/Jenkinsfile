pipeline {
    agent any

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
    }

    post {
        always {
            echo "CI pipeline complete!"
        }
    }
}
