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
                echo "====++++Test Successful++++===="
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