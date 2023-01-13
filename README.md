# Split-and-crop-images
## 하나의 이미지에서/ YOLO 좌표와 이미지를 통해/ 탐지된 객체 단위로/ 여러개의 이미지로 분할

### 사전 준비[labes의 메모장과 raw의 이미지 파일명과 정보는 서로 대치되어 있음]

** 1. labels
![212218534-667ef10c-022c-4713-9385-56f6fa689ee5](https://user-images.githubusercontent.com/101696330/212229689-79d669c9-a77c-4347-bb5b-61e5c49573a5.png)
메모장(txt) 안에 각 객체(Bounding box)의 좌표들이 YOLO 형식으로 저장되어 있음

** 2. raw
![livestock_pig_bbox_000001](https://user-images.githubusercontent.com/101696330/212219025-78606c51-71af-4759-9022-eb7b22cd4e24.jpg)
원본 이미지가 있음

** 3. yolo_processing
![livestock_pig_bbox_000001](https://user-images.githubusercontent.com/101696330/212219257-2327806e-edca-42fb-b15f-29cc6ffa4ca9.jpg)
YOLO를 거쳐 나온 결과 이미지들이 있음

### 결과
** crop
![My project-1 (1)](https://user-images.githubusercontent.com/101696330/212229395-b7fe4789-0c71-4a9b-985c-40d0b20581a0.png)
하나의 이미지에서 YOLO로 탐지된 객체(Bounding Box) 단위로 이미지를 분할해 저장됨.
