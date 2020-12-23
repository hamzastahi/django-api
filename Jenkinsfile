pipeline {
    agent {
        label'master'
	}	
    stages {
        stage("http--service"){
            stage("build") {
            steps {
                sh '''
                docker-compose build
                '''
            }
		}
        
            stage("Runing docker-compose") {
                steps {
                    sh '''
                    docker-compose up -d
                    '''
                }
            }
        }
        
        
        stage("test script") {
            steps {
                sh '''
                python3 test-http.py
                '''
            }
        }
    }
}
    
