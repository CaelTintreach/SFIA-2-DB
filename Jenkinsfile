pipeline{
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
        MYSQL_ROOT_PASSWORD = credentials('DB_PASSWORD')
    }
    stages{
        stage("Make Scripts Executable"){
            steps{
                sh 'chmod +x ./scripts/*'
            }
        }
        stage("Install Ansible and Run Playbook."){
            steps{
                sh './scripts/ansible.sh'
            }
        }
        stage("Docker deployment via stack."){
            steps{
                sh './scripts/docker.sh'
            }
        }
        stage("Deploy via swarm") {
            steps {
                sh './scripts/deploy.sh'
            }        
        }
    }
}