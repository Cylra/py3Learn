import wx

#import the newly created GUI file 
import mydemo
import myfunc

class xiFrame(mydemo.MyFrame1):
	def __init__( self, parent ):
		mydemo.MyFrame1.__init__( self, parent )

	def run_Exp( self, event ):
		client_IP   = self.m_textCtrl1.GetValue()
		client_User = self.m_textCtrl2.GetValue()
		client_Pwd  = self.m_textCtrl3.GetValue()

		server_IP   = self.m_textCtrl4.GetValue()
		server_User = self.m_textCtrl5.GetValue()
		server_Pwd  = self.m_textCtrl6.GetValue()

		run_Time = 10
		myfunc.main(server_IP, server_User, server_Pwd,
					client_IP, client_User, client_Pwd,
					run_Time)
			
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