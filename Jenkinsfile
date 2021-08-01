pipeline {
  agent {
    node {
      label 'master'
    }
  }

  options { disableConcurrentBuilds() }
  
  stages {
    stage('main') {
      steps {
        withCredentials(bindings: [
                    usernamePassword(credentialsId: 'Your_Atlassian_Credential', usernameVariable: 'SERVICEDESK_USERNAME', passwordVariable: 'SERVICEDESK_PASSWORD'),
                    usernamePassword(credentialsId: 'Your.IDrac.Username', usernameVariable: 'IDRAC_USERNAME', passwordVariable: 'IDRAC_PASSWORD'),
                  ]) {
            checkout scm
            sh '''

            # buiild docker file
            docker build -t jenkins-idrac .

            # Uploading screenshot to the ticket
            docker run --rm \
              -v ${PWD}/src:/mnt \
              -e SERVICEDESK_BASE_URL=https://yourservicedesk.url.com \
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
      string(name: 'NODE_NAME', defaultValue: '', description: 'ex) 10.104.10.43')
      string(name: 'TICKET_ID', defaultValue: '', description: 'ticket-1234')
    }
  }