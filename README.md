#DeleteGBFTweets
This is a little listener that you can run on your machine to automatically delete the tweets generated from the Granblue Fantasy Mobile Game.

Just keep it running somewhere and it'll happily listen to your tweets and automatically delete ones with "#GranblueFantasy!" hashtag.

In reality, this will work for any single hashtag you would like to delete. The target deletion hashtag can be changed in settings.py.

#How to Use
Download or clone this repository to your machine.

You can install dependencies by running
```
pip install -r requirements.txt
```

It is recommended to use a virtualenv to install the requirements.

After installing the requirements, you can run:

```
python app.py
```

To exit the program, use the hotkey CTRL + C.

#Setting Up keys
You will have to create an application that is bound to your twitter account.

You can do so at the [Twitter Apps Page](https://apps.twitter.com).
After that, the keys will be generated and you can place them in `settings.py`.
