pipeline {
  agent {
    node {
      label 'infrastructure-uge-submit-p01'
    }
  }
  stages {
    stage('main') {
      agent {
        dockerfile {
          filename 'dockerfile'
        }
      }
      steps {
        withCredentials(bindings: [
                    usernamePassword(credentialsId: 'ticket-machine.atlassian.user', usernameVariable: 'SERVICEDESK_USERNAME', passwordVariable: 'SERVICEDESK_PASSWORD'),
                    usernamePassword(credentialsId: 'idrac.user.root', usernameVariable: 'IDRAC_USERNAME', passwordVariable: 'IDRAC_PASSWORD'),
                  ]) {
            sh '''
            # Setting Environemnt Variables
            export SERVICEDESK_BASE_URL=https://help.ihme.washington.edu
            export SERVICEDESK_USERNAME=${SERVICEDESK_USERNAME}
            export SERVICEDESK_PASSWORD=${SERVICEDESK_PASSWORD}

            # Making saving directory
            mkdir -p /mnt

            cat src/main.py

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
    parameters {
      string(name: 'NODE_NAME', defaultValue: '', description: 'ex) gen-uge-archive-p123')
      string(name: 'TICKET_ID', defaultValue: '', description: 'INFR-1234')
    }
  }