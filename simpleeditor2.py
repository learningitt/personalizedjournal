#same as simpleeditor, change in the skeleton--looks more like a text editor desired
import wx

import os

ID_ABOUT=101
ID_OPEN=102
ID_SAVE=103
ID_EXIT=200



class athi(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Text Editor(Prototype v1.0)')
        panel=wx.Panel(self)
        self.control = wx.TextCtrl(self, 1, size=(500,500),style=wx.TE_MULTILINE)

        #menu and statuss bar
        status=self.CreateStatusBar()
        menubar=wx.MenuBar()
        first=wx.Menu()
        second=wx.Menu()
        third=wx.Menu()
        fourth=wx.Menu()
        
        menubar.Append(first,"File")
        
        first.Append(ID_OPEN,"Open..","For a opening a window")
        first.Append(ID_SAVE,"Save","For saving immmediate changes")
        first.Append(wx.NewId(),"Save as","For saving a new document")
        first.Append(ID_EXIT,"Exit","Exits the editor")
        
        menubar.Append(second,"Edit")
        second.Append(wx.NewId(),"Undo","To undo a change")
        second.Append(wx.NewId(),"Cut","To perform Cutting operation")
        second.Append(wx.NewId(),"Copy","To perform Copy operation")
        second.Append(wx.NewId(),"Paste","To perform Paste operation")
        second.Append(wx.NewId(),"Delete","To delete the selected portion")
        
        
        menubar.Append(third,"Format")
        third.Append(wx.NewId(),"Font","To choose from available fonts")

        
        menubar.Append(fourth,"Help")
        fourth.Append(ID_ABOUT,"About","Displays info about the application")
        
    
        self.SetMenuBar(menubar)
        #end of menu and status bar

        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, ID_EXIT, self.OnExit)
        wx.EVT_MENU(self, ID_OPEN, self.OnOpen)
        wx.EVT_MENU(self, ID_SAVE, self.OnSave)
        

        


        self.Show(1)
        
        

        self.aboutme = wx.MessageDialog( self, " A sample editor \n"
                            " in wxPython","About Sample Editor", wx.OK)
        self.doiexit = wx.MessageDialog( self, " Exit - Sure? \n",
                        "GOING away ...", wx.YES_NO)

        self.dirname = ''



    def OnOpen(self,e):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            filehandle=open(os.path.join(self.dirname, self.filename),'r')
            self.control.SetValue(filehandle.read())
            filehandle.close()
            self.SetTitle("Editing ... "+self.filename)

        dlg.Destroy()
        


        
    def OnSave(self,e):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", 
                            wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            itcontains = self.control.GetValue()
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            filehandle=open(os.path.join(self.dirname, self.filename),'w')
            filehandle.write(itcontains)
            filehandle.close()


        dlg.Destroy()

    def OnAbout(self,e):
        self.aboutme.ShowModal()

    def OnExit(self,e):
        igot = self.doiexit.ShowModal()
        if igot == wx.ID_YES:
            self.Close(True) 











        





if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=athi(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
