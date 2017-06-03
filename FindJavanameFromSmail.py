# -*- coding:utf-8 -*-
import os
import os.path
import re
import string

#获取当前目录下制定文件
#入口: 关键字
#出口: 返回指定文件的全路径
def FindCurdirfile( keyword ) :
	curdir = os.getcwd()	#获取当前目录
	filelist = os.listdir( curdir )	#列出当前文件夹下的文件和目录
	txtlist = {}
	txtlist[ 0 ] = curdir #默认返回的第0个是当前文件夹路径
	key = 1
	for filename in filelist :
		if -1 != filename.find( keyword ) :
			txtlist[ key ] = filename
			key = key + 1
	#
	if 2 < len( txtlist ) :
		for eachtxt in txtlist :
			if (eachtxt) : #第0组不显示
				print ('%02d' %(eachtxt)) + ' : ' + txtlist[eachtxt] #格式化输出字符串
		print 'which file do you want to deal with ?'
		key = int( raw_input() )
		if (key in txtlist) and (key) :
			return os.path.join( txtlist[0] , txtlist[key] )
		else :
			print 'Input Error'
			return 0
	elif 2 == len( txtlist ) : #当只有一个文件时,直接处理
		return os.path.join( txtlist[0] , txtlist[1] )
	else :
		print 'Can find any files!'
		return 0

#找到指定目录下特点后缀的文件
def FindFileType( path , isfullroot , *filetypes ) :
	result = []
	for root,dirs,files in os.walk( path ) :
		for f in files :
			if os.path.isfile(os.path.join(root,f)) and os.path.splitext(f)[1][1:] in filetypes : #os.path.join(root,f) 合成一个路径
				if False == isfullroot :
					result.append(os.path.join(root,f)[len(path)+1:])
				else :
					result.append(os.path.join(root,f))
				#print os.path.join(root,f)
	return result

if __name__ == "__main__":
	path = u'E:\\Android Something\\apktool-install-windows-r05-ibot\\QQ阅读.APK.out\\smali'
	print path
	javafilenames = []
	allfiles = FindFileType( path , False , 'smali' )

	for files in allfiles :
		lines = open( os.path.join( path , files ) , 'r').readlines()
		for line in lines :
			if '.source' in line :
				text = files + ':' + line[9:-2] + '\n'
				javafilenames.append( text )
				break

	myfile = open( 'out.txt' , 'w' )
	for javafilename in javafilenames :
		myfile.write( javafilename )
	myfile.close()
	raw_input('Program finish! Pass ENTERKEY to exit')



