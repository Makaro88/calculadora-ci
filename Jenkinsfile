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
                // Creamos el entorno virtual y usamos sus rutas absolutas
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install pytest'
                sh './venv/bin/python -m pytest'
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