# Create Blog Post With Image using ChatGPT

This little container will install 
- python
- cargo
- rustc

This project is created with devbox; first initialise it
```
devbox init
```

then then replage the generated devbox.json file by the one on this repo

or just install those packages


```
devbox add python-full@3.13.0rc1
devbox add rustc@1.79.0
devbox add cargo@1.79.0
```

enter the devbox shell

```
devbox shell
```


you need to activate the virtual environement
```
. $VENV_DIR/bin/activate
```
install those python packages

```
pip install --upgrade openai
pip install requests
```
or use the requirements file to install those packages

```
pip install -r requirements.txt
```

create an .env file and put your openAi [API Key]("https://platform.openai.com/api-keys")
```
OPENAI_API_KEY=sk-xxxxx
```


modify the value of the variable *write_blog_article_instructions* in the *article_generator.py* file

then run the script article_generator.py

```
python article_generator.py
```