'''
데이터 추출기
'''
import os
from pathlib import Path
import json

def adwav_extractor():
    # 성인대화 추출기
    training_path = Path('./training')
    validation_path = Path('./validation')
    training_label_path = Path(training_path / 'label')
    training_raw_path = Path(training_path / 'raw_data')
    tl_listdir = os.listdir(training_label_path)
    raw_listdir = os.listdir(training_raw_path)

    print(f'총 학습 데이터 파일 갯수 : {len(raw_listdir)}')
    print(f'총 레이블 데이터 파일 갯수 : {len(tl_listdir)}')
    
    

    for file in os.listdir(training_label_path):
        try:
            raw_filename = file[:-5] + '.wav'
            full_label_path = os.path.join(training_label_path, file)
            full_raw_path = os.path.join(training_raw_path, raw_filename)
            with open(full_label_path) as f:
                label = json.load(f)
            speaker1_age = int(label['Speaker1']['Age'][:2])
            speaker2_age = int(label['Speaker2']['Age'][:2])
            
            if speaker1_age >= 40 and speaker2_age >= 40:
                os.remove(full_raw_path)
                os.remove(full_label_path)
        except FileNotFoundError:
            continue
        
    print('완료되었습니다!')
    print(f'총 학습 데이터 파일 갯수 : {len(raw_listdir)}')
    print(f'총 레이블 데이터 파일 갯수 : {len(tl_listdir)}')



    
