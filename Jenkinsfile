pipeline {
    agent any

    stages {
        stage('Preparar Entorno') {
            steps {
                echo 'Verificando herramientas...'
                sh 'docker --version'
                sh 'docker compose version'
            }
        }
        
        stage('Pruebas Unitarias') {
            steps {
                echo 'Ejecutando pruebas con pytest...'
                sh 'pip3 install pytest'
                sh 'python3 -m pytest'
            }
        }

        stage('Construir Contenedores') {
            steps {
                echo 'Construyendo los contenedores de la app...'
                sh 'docker compose build'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finalizado.'
        }
    }
}