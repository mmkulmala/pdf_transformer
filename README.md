# pdf_transformer
Make pdf into image

# Init
Run following code to init project:

```python
python3 .n venv venv/
```

Then activate virtual env:
```python
source venv/bin/activate
```

# Run pdf transformer
To transform PDF into image you need give this small commandline app following parameters:
1. file = pdf file to transform
2. to = where to create the image file (for example images) 
3. type = what type of image (for example png)

Now type command below (and correct <file> <to> and <type> to some real values):
```python
python3 pdf_to_image.py <file> <to> <type>
```

You can also use flag --help to get usage info
```python
python3 pdf_to_image.py --help
```
