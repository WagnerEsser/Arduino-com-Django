# Arduino-com-Django

Trabalho de Conclusão de Curso.

Tema: Sistema para coleta de dados de condições físicas no IFC Campus Araquari utilizando Arduíno.

Instituto Federal Catarinense Câmpus Araquari.

Curso de Bacharelado em Sistemas de Informação.

* **Autor:** Wagner Esser
* **Linguagem:** Python + NoSQL
* **Ferramentas:** Django + MongoDB

---

Requerimentos:
- Instalar requerimentos do arquivo 'requirements.txt'
- Utilizar Python 3.6
    - $ sudo add-apt-repository ppa:jonathonf/python-3.6
    - $ sudo apt-get update
    - $ sudo apt-get install python3.6
- MongoDB:
    - $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
    - $ echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
    - $ sudo apt-get update
    - $ sudo apt-get install -y mongodb-org
    - $ sudo systemctl start mongodb
    - $ sudo systemctl enable mongodb
- Studio 3T Linux (antigo MongoChief) para gerenciamento no MongoDB:
    - Download em: https://studio3t.com/download-thank-you/?OS=x64
    - $ tar -xvzf studio-3t-linux-x64.tar.gz
    - $ ./studio-3t-linux-x64.sh