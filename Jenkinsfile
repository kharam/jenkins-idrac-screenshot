pipeline {
  agent {
    docker {
      label 'infrastructure-uge-submit-p01'
      image 'docker-infrapub.artifactory.ihme.washington.edu/selenium_chrome'
    }

  }

  parameters {
        string(name: 'NODE_NAME', defaultValue: '', description: 'ex) gen-uge-archive-p123')
        string(name: 'TICKET_ID', defaultValue: '', description: 'INFR-1234')
    }
  stages {
    stage('main') {
      steps {
        withCredentials([
          usernamePassword(credentialsId: 'ticket-machine.atlassian.user', usernameVariable: 'SERVICEDESK_USERNAME', passwordVariable: 'SERVICEDESK_PASSWORD'),
          usernamePassword(credentialsId: 'idrac.user.root', usernameVariable: 'IDRAC_USERNAME', passwordVariable: 'IDRAC_PASSWORD'),
        ]) {
          sh '''
            # Setting Environemnt Variables
            export SERVICEDESK_BASE_URL=https://help.ihme.washington.edu
            export SERVICEDESK_USERNAME=${SERVICEDESK_USERNAME}
            export SERVICEDESK_PASSWORD=${SERVICEDESK_PASSWORD}

            # Install requires python package for api
            pip3 install requests --usaer

            # Making saving directory
            mkdir -p /mnt

            # Uploading screenshot to the ticket
            python3 src/main.py \
                  --username "${IDRAC_USERNAME}" \
                  --password "${IDRAC_PASSWORD}" \
                  --nodename "${NODE_NAME}" \
                  --ticket "${TICKET_ID}"
          '''
        }
      }
    }

  }
}
