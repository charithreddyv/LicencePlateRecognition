# LicencePlateRecog using dakflow , opencv 

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
python TestPlates.py --video <video File name > --show <(True / False)>

```

(for all options)

```
python TestPlates.py -h 
```

