from darkflow.net.build import TFNet
import cv2
import argparse
import pytesseract
from PIL import Image
import sys
import io
import os
parser= argparse.ArgumentParser(description='Process Image for Licence Plates')
parser.add_argument('-i','--image',metavar='',required=False, help='location of the image to be processed')
parser.add_argument('-v','--video',metavar='',required=False,help='location of the video file')
parser.add_argument('-s','--show',metavar='',required=False,help='True/False to show the image output')

args = parser.parse_args()

options = {
	  'metaLoad': 'built_graph/tiny-yolo-voc-1c.meta',
	  'pbLoad': 'built_graph/tiny-yolo-voc-1c.pb',
	  'threshold': 0.02,
	  'gpu': 1.0
	}
tfnet = TFNet(options)
def get_image_path(path):
	return cv2.imread(path)
def predict_from_img(img):
	result = tfnet.return_predict(img)
	return result

def showPlates(result,img):
  for i in range(len(result)):
    br = (result[i]['topleft']['x'],result[i]['topleft']['y'])
    tl = (result[i]['bottomright']['x'],result[i]['bottomright']['y'])
    img2 = img.copy()
    img2 = cv2.rectangle(img2,tl,br,(0,255,0),7)
    cv2.imshow("image ",img2)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

def crop_image(img,result,i):
  x1 = result[i]['topleft']['x']
  y1 = result[i]['topleft']['y']
  x2 = result[i]['bottomright']['x']
  y2 = result[i]['bottomright']['y']
  width = x2-x1
  width+=20
  height = y2-y1
  height+=10
  cropped_image = img[y1:y1+height,x1:x1+width]
  return cropped_image

def enhance_image(img):
  return cv2.GaussianBlur(img,(5,5),1)
def save_img(img):
  cv2.imwrite("Image.jpg",img)
def ocr_process():
	text = pytesseract.image_to_string(Image.open('Image.jpg'))
	print("\n")
	print(text)
	print(type(text))


def show_pred_data(val,result):
	if val:
		leng = len(result)
		conf=[]
		for i in range(leng):
		  conf.append(result[i]['confidence'])
		conf.sort()
		print("\n")
		print("*** Data Related to Prediction ***")
		print("Highest confidence : ",conf[-1])
		print("actual Pred Data : ",result)
		print("***       No.of plates found => {}                       ***".format(leng))

def process_image(val,img):
  if val:
    result = predict_from_img(img)
    if len(result) >= 1:
      print("##############################################################")
      print("##### Licence Plate Found , Following up the sequenced #######")
      print("##############################################################")
      print('\n')
      showPlates(result,img)
      show_pred_data(val,result)
      for i in range(len(result)):
        cropped_image = crop_image(img,result,i)
        save_img(enhance_image(cropped_image))
        ocr_process()
    else:
      print("###############################################################")
      print("Unable to Find a LicencePlate")
      sys.exit('Terminating !')


  else:
    result = predict_from_img(img)
    if len(result) >= 1:
      print("##############################################################")
      print("##### Licence Plate Found , Following up the sequenced #######")
      print("##############################################################")
      for i in range(len(result)):
        cropped_image = crop_image(img,result,i)
        save_img(enhance_image(cropped_image))
        ocr_process()

def process_video(val,frame):
  if val:
    result = predict_from_img(frame)
    for i in range(len(result)):
      showPlates(result,frame)
      cropped_image = crop_image(frame,result,i)
      save_img(enhance_image(cropped_image))
      ocr_process()
  else:
    result = predict_from_img(frame)
    for i in range(len(result)):
      cropped_image = crop_image(frame,result,i)
      save_img(enhance_image(cropped_image))
      ocr_process()



if args.image:
  if args.image.endswith(('.jpg','.jpeg','.png','.JPEG','.JPG')):
    print("Here")
    print("Reading Image {}" .format(args.image))
    img = get_image_path(args.image)
    if args.show == 'True':
      val = True
    else:
      val = False
    process_image(val,img)
  else:
    print("cannot  Read Image")
elif args.video:
  if args.video.endswith(('.mp4','.avi','.3gp','.ogg','.flv','.AVI','.mkv')):
    cap = cv2.VideoCapture(args.video)
    if args.show == 'True':
      val = True 
    else:
      val = False
    while(cap.isOpened()):
      ret, frame = cap.read()
      process_video(val,frame)
