# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1151,729 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText_client = wx.StaticText( self, wx.ID_ANY, u"客户端", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_client.Wrap( -1 )
		self.m_staticText_client.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText_client, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText_server = wx.StaticText( self, wx.ID_ANY, u"服务器", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_server.Wrap( -1 )
		self.m_staticText_server.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText_server, wx.GBPosition( 3, 30 ), wx.GBSpan( 2, 5 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText_cIP = wx.StaticText( self, wx.ID_ANY, u"IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cIP.Wrap( -1 )
		self.m_staticText_cIP.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText_cIP, wx.GBPosition( 6, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText_sIP = wx.StaticText( self, wx.ID_ANY, u"IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_sIP.Wrap( -1 )
		self.m_staticText_sIP.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText_sIP, wx.GBPosition( 6, 31 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl1.SetMaxLength( 15 ) 
		gbSizer1.Add( self.m_textCtrl1, wx.GBPosition( 6, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl2.SetMaxLength( 15 ) 
		gbSizer1.Add( self.m_textCtrl2, wx.GBPosition( 8, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
		self.m_textCtrl3.SetMaxLength( 15 ) 
		gbSizer1.Add( self.m_textCtrl3, wx.GBPosition( 10, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl4.SetMaxLength( 15 ) 
		gbSizer1.Add( self.m_textCtrl4, wx.GBPosition( 6, 32 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl5.SetMaxLength( 15 ) 
		gbSizer1.Add( self.m_textCtrl5, wx.GBPosition( 8, 32 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
		self.m_textCtrl6.SetMaxLength( 15 ) 
		gbSizer1.Add( self.m_textCtrl6, wx.GBPosition( 10, 32 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText_cUser = wx.StaticText( self, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cUser.Wrap( -1 )
		self.m_staticText_cUser.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText_cUser, wx.GBPosition( 8, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText_sUser = wx.StaticText( self, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_sUser.Wrap( -1 )
		self.m_staticText_sUser.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText_sUser, wx.GBPosition( 8, 31 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText_cPWD = wx.StaticText( self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cPWD.Wrap( -1 )
		self.m_staticText_cPWD.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText_cPWD, wx.GBPosition( 10, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText_sPWD = wx.StaticText( self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_sPWD.Wrap( -1 )
		self.m_staticText_sPWD.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText_sPWD, wx.GBPosition( 10, 31 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"执行", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_button1.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_button1, wx.GBPosition( 6, 21 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 0 )
		
		self.m_button_clsC = wx.Button( self, wx.ID_ANY, u"重置客户端", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_button_clsC.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_button_clsC, wx.GBPosition( 8, 21 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 0 )
		
		self.m_button_clsS = wx.Button( self, wx.ID_ANY, u"重置服务器", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_button_clsS.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_button_clsS, wx.GBPosition( 10, 21 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_radioBox1Choices = [ u"30 30 30", u"40 40 40", u"50 50 50" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"运行时间(秒)", wx.DefaultPosition, wx.Size( 300,-1 ), m_radioBox1Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox1.SetSelection( 0 )
		gbSizer1.Add( self.m_radioBox1, wx.GBPosition( 11, 5 ), wx.GBSpan( 1, 26 ), wx.ALL, 5 )
		
		
		bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"选择文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gbSizer2.Add( self.m_staticText9, wx.GBPosition( 1, 26 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 450,-1 ), wx.FLP_DEFAULT_STYLE )
		gbSizer2.Add( self.m_filePicker1, wx.GBPosition( 2, 26 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"定性分析", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_button4.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_button4, wx.GBPosition( 5, 26 ), wx.GBSpan( 1, 1 ), wx.ALIGN_LEFT|wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"定量分析", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_button5.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_button5, wx.GBPosition( 5, 27 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_staticText_state = wx.StaticText( self, wx.ID_ANY, u"状态栏", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_state.Wrap( -1 )
		self.m_staticText_state.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText_state, wx.GBPosition( 8, 26 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.run_Exp )
		self.m_button_clsC.Bind( wx.EVT_BUTTON, self.clear_C )
		self.m_button_clsS.Bind( wx.EVT_BUTTON, self.clear_S )
		self.m_button4.Bind( wx.EVT_BUTTON, self.gen_PDF )
		self.m_button5.Bind( wx.EVT_BUTTON, self.gen_Excel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def run_Exp( self, event ):
		event.Skip()
	
	def clear_C( self, event ):
		event.Skip()
	
	def clear_S( self, event ):
		event.Skip()
	
	def gen_PDF( self, event ):
		event.Skip()
	
	def gen_Excel( self, event ):
		event.Skip()
	

