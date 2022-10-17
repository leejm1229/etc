conda activate <가상환경명> --> 먹히지 않으면
source ~/opt/anaconda3/etc/profile.d/conda.sh 

CONDA 환경
 
 Requiremnts.txt 생성 
   
   conda env export > conda_requirements.txt 
    
 Requiremnts.txt 와 동일한 환경 설치 
   
   conda env create -f conda_requirements.txt 
    

PIP 환경
 
 Requiremnts.txt 생성 
   
   pip freeze > requirements.txt 
    
 Requiremnts.txt 와 동일한 환경 설치 
   
   pip install -r requirements.txt
