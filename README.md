# LicencePlateRecog using dakflow , opencv 


LicencePlateRecognition : we use darkflow (yolo) object detection api for detecting a licence plate in a image then crop the image to process the data in the cropped image.

Here We use pytesseract for detecting ocr data in image , just some modification's in the code you  can use any ocr detection algorithm example use could use GoogleVisionApi too

This Code now works for Images and videos 

Please Follow the enlisted commands below to make the program up and running 

``` 
cd Licence_plate_Recognition
```


``` 
virtualenv venv
```
``` 
source venv/bin/activate
```
```
pip install -r requirements.txt
```

``` 
pip install . 
```
```
source env.sh
```

#usage
```
python TestPlates.py -i <path_to_img>
```
(or)

```
python TestPlates.py --image <path_to_img>
```
(processing video's)
```
python TestPlates.py --video <path to video >
```


To show Processing Images/Frames

```
python TestPlates.py --video <video File name > --show True/False

```

(for all options)

```
python TestPlates.py -h 
```

