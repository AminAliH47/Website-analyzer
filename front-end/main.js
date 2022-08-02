const {
    app,
    BrowserWindow
} = require('electron')

const createWindow = () => {
    const win = new BrowserWindow({
        width: 1024,
        height: 600,
        'minWidth': 800,
        'minHeight': 550,
        'maxWidth': 1024,
        'maxHeight': 700,
    })

    win.loadFile('index.html')
}

app.whenReady().then(() => {
    createWindow()
})