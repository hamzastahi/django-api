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
	         docker-compose up -d
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
}
    
