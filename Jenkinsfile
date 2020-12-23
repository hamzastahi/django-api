pipeline {
    agent {
          label'master'
	}	
    stages {
	stage("http--service1") {
	
	parallel {
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
	         docker-compose up
                  '''
			 }
			}
		}
       
	}
   }
	post {
          success {
            sh 'python3 test-http.py'	
          }
          failure {
            echo 'failure'
          }
	}
}
    
