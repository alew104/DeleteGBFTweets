# DeleteGBFTweets
This is a little listener that you can run on your machine to automatically delete the tweets generated from the Granblue Fantasy Mobile Game.

Just keep it running somewhere and it'll happily listen to your tweets and automatically delete ones with "#GranblueFantasy!" hashtag.

In reality, this will work for any single hashtag you would like to delete. The target deletion hashtag can be changed in settings.py.

Backup requests are currently supported. Other GBF Raid Finder sites still pick up your backup requests.

You'll need to have a public Twitter account for this bot to work.

# How to Use
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

# Setting Up Keys
You will have to create an application that is bound to your twitter account.

You can do so at the [Twitter Apps Page](https://apps.twitter.com).
After that, the keys will be generated and you can place them in `settings.py`.

# Non-Listener Version
The non-listener version checks your tweets every two minutes for Granblue Fantasy tagged tweets. It does NOT delete backup raid requests.
