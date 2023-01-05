import cv2, glob, os, time
import pybboxes as pbx

if __name__ == '__main__':
    # 폴더의 모든 이미지 불러오기
    root_dir = "./dataset/" # Enter Directory of all images
    raw_imgs = glob.glob(os.path.join(root_dir, "raw/","*.jpg"), recursive=True)    
    raw_imgs = sorted(raw_imgs)
    crop_img = None

    for img in raw_imgs:    # 모든 이미지에 대해 반복
        # 메모장 읽기
        f = open(root_dir+"labels/"+img.split("\\")[1].split(".")[0]+".txt", 'r')
        strings = f.readlines()
        f.close()

        # 메모장 전처리
        strings_list = list()
        for i in range(len(strings)):
            strings[i] = strings[i].replace('\n', '')
            strings[i] = strings[i][2:]
            strings_list.append(strings[i].split(" "))  # YOLO형식 bounding box 좌표
        
        # 이미지 읽기
        img_cv = cv2.imread(img)
        height, width = img_cv.shape[:2]   # 이미지의 높이와 너비

        img = img.split('\\')[1].replace('.jpg', '').replace('.png', '').replace('.jpeg', '').replace('.bmp', '')   # 파일명만 남기기
        # yolo형식 bounding box 좌표를 voc형식으로 변환
        for idx, bbox in enumerate(strings_list):   
            yolo_bbox = (float(bbox[0]), float(bbox[1]), float(bbox[2]), float(bbox[3]))   
            x, y, w, h = pbx.convert_bbox(yolo_bbox, from_type="yolo", to_type="voc", image_size=(width, height))
            # 이미지 자르기
            crop_img = img_cv[y:h, x:w]   # y, h, x, w
            # 이미지 저장
            cv2.imwrite(root_dir+"crop/"+img+'_'+str(idx+1)+".jpg", crop_img)
        
        time.sleep(0.2)