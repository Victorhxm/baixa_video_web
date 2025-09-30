from flask import Flask, render_template, request, session
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path


app = Flask(__name__)

@app.route('/')           

def entry_page() -> 'html': # type: ignore
    return render_template('entry.html',
                           the_title = 'Baixa vídeo do Youtube')

@app.route('/baixado', methods=['POST'])
def do_url() ->  'html':
   
   url = request.form['url']
   link = url
   video = YouTube(link,on_progress_callback=on_progress)
   stream = video.streams.get_highest_resolution()
   DOWNLOADS = Path.home() / 'Downloads'
   stream.download(DOWNLOADS)
    
   return render_template('ok.html', url = url, )


if __name__=='__main__':
    app.run(debug=True)
   