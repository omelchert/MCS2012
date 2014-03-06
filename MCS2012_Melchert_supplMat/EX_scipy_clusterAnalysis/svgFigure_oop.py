## \file   svgFigure_oop.py
#  \brief  class that implements useful functions
# 	   for plotting svg files
#	   
#  supplementary material MCS2012
#
#  \author OM
#  \date   03.02.11
import sys

class mySVG:
	"""scalable vector graphics scene description 
	
	implements various functions that might be used to produce
	a .svg figure
	"""


	def __init__(self,x0=0.,y0=0.,width=100.,heigth=100.):
		"""default constructor for instance of object mySVG"""
		self._x0 = x0
		self._y0 = y0
		self._w  = width
		self._h  = heigth
		self._sceneDescription=""

	def __str__(self):
		# write header to scene description string 
		myScene  = "<svg width=\"%lf\" height=\"%lf\" viewBox=\" %lf %lf %lf %lf\" >\n"%\
			   (self._w, self._h,self._x0,self._y0,self._x0+self._w,self._y0+self._h)
		# add actual content of the svg figuer
		myScene += self._sceneDescription
		# add footer to scene description
		myScene += "</svg>\n"
		return myScene

	def rectangle(self,x,y,w,h,width=1.,col='black',fillCol='none',so=1.,fo=1.):
		"""add rectangle to scene description
		
		Input:
		x,y	- x and y position of the rectangles center 
		w,h	- width and hight of the rectangle 
		width	- width of the boundary line
		col	- color of the line
		fillCol	- fill color of the rectangle 
		so	- fill opacity 
		fo	- stroke opacity
		"""
		x=x-0.5*w
		y=y-0.5*h
		self._sceneDescription += "<rect x=\"%lf\" y=\"%lf\" width=\"%lf\" height=\"%lf\"\
				\n\tstyle=\"stroke-width: %lf;\
				\n\tstroke: %s;\
				\n\tfill: %s;\
				\n\tfill-opacity: %lf;\
				\n\tstroke-opacity: %lf;\"/>\n"%(x,y,w,h,width,col,fillCol,fo,so)

	def line(self,x1,y1,x2,y2,width=1.,col='black'):
		"""add line to scene description
		
		Input:
		x1,y1	- x and y position of the start of the line
		x2,y2	- x and y position of the end of the line
		width	- width of the boundary line
		col	- color of the line
		"""
		self._sceneDescription += "<line x1=\"%lf\" y1=\"%lf\" x2=\"%lf\" y2=\"%lf\"\
				\n\tstyle=\"stroke-width: %lf;\
                                \n\tstroke-linecap: round;\
				\n\tstroke: %s;\"/>\n"%(x1,y1,x2,y2,width,col)

	def circle(self,cx,cy,r,width=1,col='black',fillCol='none'):
		"""add circle to scene description
		
		Input:
		cx,cy	- x and y position of the center of the circle
		r	- radius of the circle
		width	- width of the boundary line
		col	- color of the line
		fillCol	- fill color of the circle
		"""
		self._sceneDescription += "<circle cx=\"%lf\" cy=\"%lf\" r=\"%lf\"\
				\n\tstyle=\"stroke-width: %lf;\
				\n\tstroke: %s;\
				\n\tfill:%s;\"/>\n"%(cx,cy,r,width,col,fillCol)

	def path(self,xyList,width=1.,col='black'):
		"""add path to scene description
		
		Input:
		xyList	- list of xy data points
		width	- width of the line
		color	- color of the line
		"""
		myStr=  "<path d=\"M "
		for xy in xyList[:-2]:
			myStr+= "\t%lf %lf L\n"%(xy[0],xy[1])
		myStr+= "\t%lf %lf \" \
				\n\tstyle=\"stroke-width: %lf;\
				\n\tstroke:%s;\
				\n\tstrike-linecap:round;\
				\n\tstroke-linejoin: round;\
				\n\tfill:none\"/>\n"%(xyList[-1][0],xyList[-1][1],width,col)
		self._sceneDescription += myStr

	def text(self,x,y,size,myText,dx=0.,dy=0.,rot=0.):
                myStr = "<text x=\"%lf\" y=\"%lf\"  dx=\"%lf\" dy=\"%lf\" font-size=\"%lf\" transform=\"rotate(%lf %lf,%lf)\"  >%s</text>\n"%(x,y,dx,dy,size,rot,x,y,myText)
		self._sceneDescription += myStr

	def saveFile(self,fileStream=sys.stdout):
		"""dump scene description to specified file stream"""
		fileStream.write("%s"%(self))



if __name__=='__main__':
	myFigure = mySVG(width=150,heigth=100)
	
	myFigure.line(0,20,20,30)
	myFigure.circle(50,50,30,2,fillCol='red')
	myFigure.rectangle(100,50,30,50,2,fillCol='green')

	myFigure.saveFile()

