#text editor to open,save text files in notepad
import wx

import os


ID_ABOUT=101
ID_OPEN=102
ID_SAVE=103
ID_BUTTON1=300
ID_EXIT=200
class athi(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,wx.ID_ANY, "jbj")
        self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        self.CreateStatusBar()


        filemenu= wx.Menu()

        filemenu.Append(ID_OPEN, "&Open"," Open a file to edit")
        filemenu.AppendSeparator()
        filemenu.Append(ID_SAVE, "&Save"," Save file")
        filemenu.AppendSeparator()
        filemenu.Append(ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(ID_EXIT,"E&xit"," Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") 
        self.SetMenuBar(menuBar)


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
