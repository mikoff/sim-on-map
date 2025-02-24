from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from folium.plugins import Draw
import folium, io, sys, json

if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv)
    
    m = folium.Map(location=[61.78491, 34.34691], zoom_start=15)
    
    draw = Draw(
        draw_options={
            'polyline':True,
            'circle':False,
            'marker':False,
            'circlemarker':False},
        edit_options={'edit':False})
    m.add_child(draw)

    data = io.BytesIO()
    m.save(data, close_file=False)

    class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
       def javaScriptConsoleMessage(self, level, msg, line, sourceID):
          coords_dict = json.loads(msg)
          coords = coords_dict['geometry']['coordinates']
          for p in coords:
              lat, lon = p[0], p[1]
              print(f'{lat:.8f} {lon:.8f}')

    view = QtWebEngineWidgets.QWebEngineView()
    page = WebEnginePage(view)
    view.setPage(page)
    view.setHtml(data.getvalue().decode())
    view.show()
    sys.exit(app.exec_())
