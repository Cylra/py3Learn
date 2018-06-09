import wx

class Frame(wx.Frame):
	def __init__(self,image,parent = None,id = -1,pos = wx.DefaultPosition,title = "可视化图形分析"):
		#显示图片
		tmp = image.ConvertToBitmap() 
		size = tmp.GetWidth(),tmp.GetHeight()
		wx.Frame.__init__(self,parent,id,title,pos,size)
		self.bmp = wx.StaticBitmap(parent=self, label=tmp)

class App(wx.App):
	def OnInit(self):
		#图片处理
		image = wx.Image("test.jpg",wx.BITMAP_TYPE_JPEG) 
		self.frame = Frame(image)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True


def main():
	app = App()
	app.MainLoop()


if __name__ == '__main__':
	main()