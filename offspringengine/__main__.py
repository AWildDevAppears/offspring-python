import webview

from offspringengine.expose import expose_to


def main():
    window = webview.create_window("Hello world", "http://localhost:5173")

    webview.start(expose_to, window, debug=True)




main()
