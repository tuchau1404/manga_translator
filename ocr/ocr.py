from paddleocr import PaddleOCR,draw_ocr
import json

def predict_path(img_path):  
    det_dir = "ocr/models/en_PP-OCRv3_det_infer/"  
    rec_dir = "ocr/models/en_PP-OCRv3_rec_infer/"
    ocr = PaddleOCR(use_angle_cls=False,lang='en',det_model_dir=det_dir,rec_model_dir=rec_dir)

    result = ocr.ocr(img_path, cls=True)
    # print(result[0][1][0])
    dict = {}
    for i, line in enumerate(result):
        dict[i]={}
        dict[i]['det']={}
        for j in range(1,5):
            dict[i]['det'][j]={}
            dict[i]['det'][j]['x']=str(int(result[i][0][j-1][0]))
            dict[i]['det'][j]['y']=str(int(result[i][0][j-1][1]))
        dict[i]['rec']={}
        dict[i]['rec']['text']=result[i][1][0]
        dict[i]['rec']['confidence']=str(result[i][1][1])

    with open("output/result.json", "w") as f:
        json.dump(dict, f)

predict_path("assets/ppocr_img/imgs_en/img623.jpg")