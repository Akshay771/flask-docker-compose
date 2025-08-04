DOCKER COMPOSE UP KAISE USE KARE

# clone kare github repo ko apne local system pe
$ git clone https://github.com/Akshay771/flask-docker-compose.git

# docker installed hona chahiye already
  first time build kare

$ sudo docker compose build

# containers up kare first time
$ sudo docker compose up

# all container stop/down kare
$ sudo docker compose down

# ab flask/app.py me new route add kare 
  @app.route('/v3')
  def testV3():    
      return jsonify({"message":"testing V3 Route"})

# phir se containers up kare bina build kare
$ sudo docker compose up

# ab ye URL open kare
  http://localhost/v3

