pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Let\'s build the image'
        sh 'docker build -t myapp:0.1 .'
      }
    }

    stage('Runnning the image') {
      steps {
        echo 'Running the image'
        sh 'docker run --name myflaskcontainer -d -p 5000:5000 myapp:0.1'
      }
    }

    stage('Final') {
      steps {
        sh 'docker container rm -f $(docker container ls -qa)'
        sh '''docker rmi myapp:0.1


'''
      }
    }

  }
}