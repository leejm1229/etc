# 이럴 경우 port 8000과 관련된 모든 프로세스를 죽이고 다시 실행시키면 된다.
# Mac에서는 터미널에서 "sudo lsof -t -i tcp:8000 | xargs kill -9"를 입력하면 된다.

# 그리고 다시 "python manage.py runserver"를 통해 장고 runserver를 실행시키면 에러 메시지가 사라진다.
