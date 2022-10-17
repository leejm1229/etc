# 설치를 완료했다면, 먼저 아래의 명령어를 입력해주자.

# brew install mysql
# 그다음 아래의 명령어로 OpenSSL을 설치해 준다.

# brew install openssl
# 설치가 완료된 후, 아래의 명령어로 mysqlclient를 설치해 준다.

# LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient
# -----------------------------------------------------------------------

#  models.py --> 아래 코드처럼 이미 db에 있는 정보를 가져올 때는 managed = False로 지정
class JejuOlle(models.Model):
    course = CharField(max_length=10)
    course_name = CharField(max_length=20)
    distance = FloatField()
    time_info = CharField(max_length=10)
    start_end_info = CharField(max_length=30)
    cre_date = DateField()

    class Meta:
        db_table = 'jeju_olle'
        app_label = 'thirdapp'
        managed = False

        
        
        
# 장고는 기본적으로 sqlite로 연결되어 있지만 maria DB 연결을 위해서
# 프로젝트 settings.py에서 추가

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'custom': { # thirdapp에서 사용할 데이터베이스 설정 추가
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'human',
        'USER': 'human',
        'PASSWORD': '1234',
        'HOST': '15.164.153.191',
        'PORT': 3306
    }
}
DATABASE_ROUTERS = ['thirdapp.router.DBRouter']





# 그리고 해당앱에서 router.py를 생성한 후 아래코드 작성
# 단 label과 db명은 상황에 따라 바꿔준다.
# 해당앱의 router.py 
class DBRouter:
    def db_for_read(self, model,**hints):
        if model._meta.app_label == 'thirdapp':
            return 'custom'
        return None
        
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'thirdapp':
            return 'custom'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'thirdapp' or obj2._meta.app_label == 'thirdapp':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'thirdapp':
            return db == 'custom'
        return None

      
