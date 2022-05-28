import tensorflow as tf
from pycoral.utils.dataset import read_label_file
from pycoral.adapters import detect
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import cv2
from pycoral.adapters import common
import numpy as np

model = r"C:\teste\TCC\COUNT\counteyeapi\tensor\beegeye_efficientdetline_objectDetection_80Epoc_64BZ.tflite"
labels = read_label_file("C:/Users/julia/OneDrive/Área de Trabalho/Pirai/label_line_objectDetection.txt")

def teste(INPUT_IMAGE):

  def draw_objects(draw, objs, scale_factor, labels):
    
    COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype=np.uint8)
    for obj in objs:
      bbox = obj.bbox
      color = tuple(int(c) for c in COLORS[obj.id])
      draw.rectangle([(bbox.xmin * scale_factor, bbox.ymin * scale_factor),
                      (bbox.xmax * scale_factor, bbox.ymax * scale_factor)],
                    outline=color, width=3)
      font = ImageFont.truetype(r"c:\windows\fonts\arial.ttf")
      draw.text((bbox.xmin * scale_factor + 4, bbox.ymin * scale_factor + 4),
                '%s\n%.2f' % (labels.get(obj.id, obj.id), obj.score),
                fill=color, font=font)

      print('obj: ',obj)
      print('label: ',labels.get(obj.id, obj.id))


    predict = {
      "class": "Desconhecido"
    }

    # try:
    #     classes, scores, boxes = model.detect(cap, 0.1, 0.2)
    #     for (classid, score, box) in zip(classes, scores, boxes):
    #         predict = {
    #             "class": class_names[0],
    #             "accuracy": score
    #         }
    # except Exception as ex:
    #     pass

    return predict

  interpreter = tf.lite.Interpreter(model)
  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()
  interpreter.allocate_tensors()

  interpreter.invoke()


  image = Image.open(INPUT_IMAGE)
  _, scale = common.set_resized_input(interpreter, image.size, lambda size: image.resize(size, Image.ANTIALIAS))
  interpreter.invoke()
  objs = detect.get_objects(interpreter, score_threshold=0.2, image_scale=scale)

  display_width = 800
  scale_factor = display_width / image.width
  height_ratio = image.height / image.width
  image = image.resize((display_width, int(display_width * height_ratio)))

  draw_objects(ImageDraw.Draw(image), objs, scale_factor, labels)

  

