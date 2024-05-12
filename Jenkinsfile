pipeline {

  agent any
  triggers {
        pollSCM '* * * * *'
    }
  stages {  // Define the individual processes, or stages, of your CI pipeline

    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
          sh """
          apt-get update
          apt-get -y install python3
          apt-get -y install python3.11-venv
          python3 -m venv ./network_automation/venv
          . ./network_automation/venv/bin/activate
          cd ./network_automation
          pwd
          pip3 install -r ./req.txt
          pip3 install pylint
          pip3 install autopep8
          pip3 install autoflake


          """
        }
      }
    }
    stage('Linting') { // Run pylint against your code
      steps {
        script {
          sh """
          . ./network_automation/venv/bin/activate
          cd ./network_automation
          pylint *.py
          autopep8 --in-place --aggressive --aggressive *.py
          autoflake -r --in-place --remove-unused-variables *.py
          """
        }
      }
    }
    stage('Testing') { // Perform  testing
      steps {
        script {
          sh """
          . ./network_automation/venv/bin/activate
          cd ./network_automation
          sed -i -r "s/(hostname .*)/hostname : '192.168.56.101'/g" Configuration_Data/host.yaml
          echo "1\n1\n1\n2\n2\n1\n2\n2\n3\n1\n3\n2\n0\n" > all_possible_inputes
          python3  ./main.py < ./all_possible_inputes
          """
        }
      }
    }
    stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}