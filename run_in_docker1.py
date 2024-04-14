import subprocess

# Запуск Docker daemon с использованием драйвера "vfs"
subprocess.Popen(['/usr/bin/sudo', '/usr/bin/dockerd', '--host=unix:///var/run/docker.sock', '--host=tcp://0.0.0.0:2375', '--storage-driver=vfs'])

# Сборка Docker-образа
subprocess.run(['sudo', 'docker', 'build', '-t', 'font-recognition', '.'])

# Запуск Docker-контейнера
subprocess.run(['sudo', 'docker', 'run', '--gpus', 'all', '-v', '/content/font_recognition_model.h5:/path/to/model/checkpoint', '-v', '/content/output_dir/test/better-vcr-5.2/better-vcr-5.2_17.jpg:/path/to/image/file', 'font-recognition'])