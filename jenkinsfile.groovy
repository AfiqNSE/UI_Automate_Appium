pipeline {
    agent any
    stages {
        stage("Appium Server"){
            steps{
                build job: 'jenkins_appiumServer_poc', wait: false
            }
        }
        stage("Start Emulator"){
            steps{
                build job: 'jenkins_androidEmu_poc', wait: false
            }
        }
        stage("POC Test"){
            steps{
                build job: 'jenkins_test_poc', wait: true
            }
        }
    }
    post{
        success {
                echo 'POC Done'
            }
        }
}