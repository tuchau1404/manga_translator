from paddleocr import PaddleOCR,draw_ocr
det_dir = "ocr/models/en_PP-OCRv3_det_infer/"  
rec_dir = "ocr/models/en_PP-OCRv3_rec_infer/"
ocr = PaddleOCR(use_angle_cls=True,lang='en',det_model_dir=det_dir,rec_model_dir=rec_dir)
img_path = 'assets/001-fix-2.jpg'
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)


# draw result
from PIL import Image
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='assets/ppocr_img/fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('output/result.jpg')