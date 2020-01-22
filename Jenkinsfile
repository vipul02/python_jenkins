pipeline {
    agent any
    stages {

       
        stage('Build') {
            steps {
                echo "====++++Building Successful++++===="
                bat 'python --version'
                
            }
        }

        stage('Test') {
            steps {
                echo "====++++Test Successful++++===="
                bat 'python -m unittest'
            }
        }

        stage('Deploy') {
            steps {
                echo "====++++Deployed Successfully++++===="
            }
        }
    }
}