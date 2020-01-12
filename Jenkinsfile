pipeline{
        agent any
        
        stages{
		stage('--Build Docker--'){
			steps{
				      '''docker-compose up -d --build
				      docker ps -a
				      '''
			}
		}
                stage('--Deploy Docker--'){
                        steps{
                                sh '''ssh qa-project-two  << BOB
				      export BUILD_NUMBER="${BUILD_NUMBER}"
                                      docker service update --replicas 3 --image ansible-jenkins-project2:5000/service1:build-${BUILD_NUMBER} project_service1
				      docker service update --replicas 3 --image ansible-jenkins:5000/service2:build-${BUILD_NUMBER} project_service2
				      docker service update --replicas 3 --image ansible-jenkins:5000/service3:build-${BUILD_NUMBER} project_service3
				      docker service update --replicas 3 --image ansible-jenkins:5000/service4:build-${BUILD_NUMBER} project_service4
                                      '''
                        }
                }
        }
}
