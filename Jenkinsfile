pipeline {
  agent {
    docker {
      image 'docker-infrapub.artifactory.ihme.washington.edu/selenium_chrome'
    }

  }
  stages {
    stage('main') {
      steps {
        sh 'echo \'hi\''
      }
    }

  }
}