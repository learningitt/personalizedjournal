#media player to play mp3 audio files
import wx
import wx.media
import os
class Panel1(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,-1,style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
        try:
            self.mc=wx.media.MediaCtrl(self,style=wx.SIMPLE_BORDER)
        except NotImplementError:
            self.Destroy()
            raise
        offset=0
        
        loadButton=wx.Button(self,-1,"Load File")
        self.Bind(wx.EVT_BUTTON,self.onLoadFile,loadButton)

        playButton = wx.Button(self,-1,"Play")
        self.Bind(wx.EVT_BUTTON, self.onPlay,playButton)

        pauseButton = wx.Button(self,-1,"Pause")
        self.Bind(wx.EVT_BUTTON, self.onPause,pauseButton)

        stopButton = wx.Button(self,-1,"Stop")
        self.Bind(wx.EVT_BUTTON, self.onStop,stopButton)  
        

       
        self.st_file = wx.StaticText(self, -1, ".mp3 ", size=(200,-1))
        self.st_size = wx.StaticText(self, -1, size=(100,-1))
        self.st_len  = wx.StaticText(self, -1, size=(100,-1))
        self.st_pos  = wx.StaticText(self, -1, size=(100,-1))
        
        
        sizer = wx.GridBagSizer(5,5)
        sizer.Add(loadButton, (1,1))
        sizer.Add(playButton, (2,1))
        sizer.Add(pauseButton, (3,1))
        sizer.Add(stopButton, (4,1))
        sizer.Add(self.st_file, (1, 2))
        sizer.Add(self.st_size, (2, 2))
        sizer.Add(self.st_len,  (3, 2))
        sizer.Add(self.st_pos,  (4, 2))
        sizer.Add(self.mc, (5,1), span=(5,1))  
        self.SetSizer(sizer)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onTimer)
        self.timer.Start(100)
        
    def onLoadFile(self, evt):
        dlg = wx.FileDialog(self, message="Choose a media file",
                            defaultDir=os.getcwd(), defaultFile="",
                            style=wx.OPEN | wx.CHANGE_DIR )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.doLoadFile(path)
        dlg.Destroy()
        
    def doLoadFile(self, path):
        if not self.mc.Load(path):
            wx.MessageBox("Unable to load %s: Unsupported format?" % path, "ERROR", wx.ICON_ERROR | wx.OK)
        else:
            folder, filename = os.path.split(path)
            self.st_file.SetLabel('%s' % filename)
            self.mc.SetInitialSize()
            self.GetSizer().Layout()
            self.mc.Play()
        
    def onPlay(self, evt):
        self.mc.Play()
    
    def onPause(self, evt):
        self.mc.Pause()
    
    def onStop(self, evt):
        self.mc.Stop()
    
    def onSeek(self, evt):
        pass
        
        
    def onTimer(self, evt):
        offset = self.mc.Tell()
        self.st_size.SetLabel('size: %s ms' % self.mc.Length())
        self.st_len.SetLabel('( %d seconds )' % (self.mc.Length()/1000))
        self.st_pos.SetLabel('position: %d ms' % offset)
        
      
app = wx.PySimpleApp()

frame = wx.Frame(None, -1, "play audio files", size = (320, 350))

Panel1(frame, -1)
frame.Show(1)
app.MainLoop()
