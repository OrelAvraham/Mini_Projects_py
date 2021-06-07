import webbrowser

sub = input('Enter the subject:' ).replace(' ', '-')

url = f'https://fightlist.info/en/{sub}.html'
webbrowser.register('chrome',
    None,     
    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe")) 
webbrowser.get('chrome').open(url)

if __name__ == '__mani__':
    pass