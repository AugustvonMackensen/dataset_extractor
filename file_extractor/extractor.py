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
    valid_label_path = Path(validation_path / 'label')
    valid_raw_path = Path(validation_path / 'raw_data')
    tl_listdir = os.listdir(training_label_path)
    raw_listdir = os.listdir(training_raw_path)
    vl_dir = os.listdir(valid_label_path)
    vr_dir = os.listdir(valid_raw_path)

    print(f'총 학습 데이터 파일 갯수 : {len(raw_listdir)}')
    print(f'총 학습 레이블 데이터 파일 갯수 : {len(tl_listdir)}')
    print('추리기 시작합니다!')
    
    for file in tl_listdir:
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
        
    print('추리기 완료되었습니다!')
    print(f'총 학습 데이터 파일 갯수 : {len(raw_listdir)}')
    print(f'총 학습 레이블 데이터 파일 갯수 : {len(tl_listdir)}')
    
    print(f'총 검증 데이터 파일 갯수 : {len(vr_dir)}')
    print(f'총 검증 레이블 데이터 파일 갯수 : {len(vl_dir)}')
    print('추리기 시작합니다!')

    for file in vl_dir:
        try:
            raw_filename = file[:-5] + '.wav'
            full_label_path = os.path.join(valid_label_path, file)
            full_raw_path = os.path.join(valid_raw_path, raw_filename)
            with open(full_label_path) as f:
                label = json.load(f)
            speaker1_age = int(label['Speaker1']['Age'][:2])
            speaker2_age = int(label['Speaker2']['Age'][:2])
            
            if speaker1_age >= 40 and speaker2_age >= 40:
                os.remove(full_raw_path)
                os.remove(full_label_path)
        except FileNotFoundError:
            continue
    
    print('추리기 완료되었습니다!')
    print(f'총 검증 데이터 파일 갯수 : {len(vr_dir)}')
    print(f'총 검증 레이블 데이터 파일 갯수 : {len(vl_dir)}')