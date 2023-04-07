'''
깃 허브 : 소스코드를 올리는 어떤 공간
깃 : 소스코드를 내 컴퓨터에서 인터넷으로 올려주는 역할

그러므로 git은 따로 설치해줘야 한다.

토큰

git 초기 설정
git config --global user.name “user.name”
git config --global user.email “user.email”
git config --global core.autocrlf input(window는 true)  운영체제 마다 줄 바꿈이 달라서 세팅해준다.

git config --list (셋팅 정보확인)

git init (git을 쓸 준비 내가 초기화를 해주겠다.)  맨처음에 프로젝트를 올릴 때
 폴더를 하나 만들고 git init을 해주면 그 폴더는 git 전용 폴더가 된다…
ls -la을 해주면 .git이라는 숨겨진 파일이 보인다.
만약 git을 삭제하고 싶으면 rm -rf .git  이러면 이 폴더는 그냥 더이상 깃 폴더가 아니게 된다.

git add .  어떤 파일을 깃에 올릴지 보자 //  여기서 .은 모두 파일을 의미
만약 index.html 파일만 올리고 싶으면 git add index.html 이라고 작성

git status    상태를 알려주는 명령어 (어떤 파일이 추가가 되었는지)

git commit -m “first commit”  히스토리를 만들어 내는 것(“”안에 들어가는 것은 내가 지정”)

깃 허브에 보내는 방법
git remote add origin https://github.com/jeongmin1229/test.git
 연결시켜 주기 이것은 repository에 들어가면 나와있음

git remote -v   연결상태 확인

git push -u origin main  보내는 법



만약 추가된 코드를 보내고 싶다면 
git add .  여기서는 git init 을 해줄 필요 X
git commit -m “second commit”  히스토리를 만들어 준다.
git push -u origin main

반대로 코드를 내 컴퓨터로 가져오는 방법
git clone 주소

만약 남의 코드에 올리고 싶다.
그런데 내가 최종 승인자가 아니라면
git checkout -b '이름'
git push origin 

사용자 변경하는 법
git checkout -m '이름'

깃 폴더 삭제
rm -rf .git

만약 git push 후
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/leejm1229/java-hanati.git'
이런 오류가 난다면 명령어에 git push origin +main을 입력하면 된다.
'''










