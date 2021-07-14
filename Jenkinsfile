pipeline {
  agent {
    node {
      label 'infra'
    }
  }

  options { disableConcurrentBuilds() }
  
  stages {
    stage('main') {
      steps {
        withCredentials(bindings: [
                    usernamePassword(credentialsId: 'ticket-machine.atlassian.user', usernameVariable: 'SERVICEDESK_USERNAME', passwordVariable: 'SERVICEDESK_PASSWORD'),
                    usernamePassword(credentialsId: 'idrac.user.root', usernameVariable: 'IDRAC_USERNAME', passwordVariable: 'IDRAC_PASSWORD'),
                  ]) {
            checkout scm
            sh '''

            # buiild docker file
            docker build -t jenkins-idrac .

            # Uploading screenshot to the ticket
            docker run --rm \
              -v ${PWD}/src:/mnt \
              -e SERVICEDESK_BASE_URL=https://help.ihme.washington.edu \
              -e ATLASSIAN_USERNAME=${SERVICEDESK_USERNAME} \
              -e ATLASSIAN_PASSWORD=${SERVICEDESK_PASSWORD} \
              -t jenkins-idrac python3 /mnt/main.py \
              --username "${IDRAC_USERNAME}" \
              --password "${IDRAC_PASSWORD}" \
              --nodename "${NODE_NAME}" \
              --ticket "${TICKET_ID}"
          '''
          }

        }
      }

    }
    parameters {
      string(name: 'NODE_NAME', defaultValue: '', description: 'ex) gen-uge-archive-p123')
      string(name: 'TICKET_ID', defaultValue: '', description: 'INFR-1234')
    }
  }