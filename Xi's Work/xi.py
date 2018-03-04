import wx

#import the newly created GUI file 
import mydemo

class xiFrame(mydemo.MyFrame1):
	def __init__( self, parent ):
		mydemo.MyFrame1.__init__( self, parent )

	def run_Exp( self, event ):
		pass
			
	def clear_C( self, event ):
		self.m_textCtrl1.Clear()
		self.m_textCtrl2.Clear()
		self.m_textCtrl3.Clear()
	
	def clear_S( self, event ):
		self.m_textCtrl4.Clear()
		self.m_textCtrl5.Clear()
		self.m_textCtrl6.Clear()
	
app = wx.App(False)
frame = xiFrame(None)
frame.Show()
app.MainLoop()