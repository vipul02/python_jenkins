pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "====++++Building Successful++++===="
                sh 'python --version'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest'
            }
        }

        stage('Deploy') {
            steps {
                echo "====++++Deployed Successfully++++===="
            }
        }
    }
}