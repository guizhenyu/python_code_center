//bilinear interpolation method for resize(zoom)
void onBilinear(CDib &m_Dib,BYTE **srcImg,BYTE **dstImg,int h, int w,double zoomNumber)
{
	int ey,ex;
	int j,i;
	int zoomH = (int)(zoomNumber*h + 0.5);
	int zoomW = (int)(zoomNumber*w + 0.5);
	int originalLineByte = ((w % 4 == 0 ? w : w + (4 - (w % 4)))*m_Dib.GetBitCount())/8; //align the width
	int zoomLineByte = ((zoomW % 4 == 0 ? zoomW : zoomW + (4 - (zoomW % 4)))*m_Dib.GetBitCount())/8;
	BYTE *temp = new BYTE[w * h];
 
	for(j=0;j<h;j++) //copy original image to the buffer
	{
		for(i=0;i<w;i++)
		{
			temp[j*w+i] = srcImg[j][i];  
		}
	}
 
	BYTE *newImg = new BYTE [zoomLineByte * zoomH];
 
	for(ey = 0;ey < zoomH;ey++)
	{
		for(ex = 0;ex < zoomLineByte;ex++)
		{
			double jz = ((double)ey)/zoomNumber;  //get the original image coordinates
			double iz = ((double)ex)/zoomNumber;
			int j1 = (int)jz;
			int i1 = (int)iz;
			int j2 = j1 + 1;
			int i2 = i1 + 1;
			double u = iz - i1;					//插值点与邻近整数点(j1,i1)的距离 x coordinate
			double v = jz - j1;					// y coordinate
 
			double s1 = (1.0 - u)*(1.0 - v);    //邻近整数点(j1,i1)函数值的系数（左上角）left-up corner
			double s2 = (1.0-u)*v;				//邻近整数点(j1,i1)函数值的系数（左下角）left-down corner
			double s3 = u*(1.0 - v);			//邻近整数点(j1,i1)函数值的系数（右上角）right-up corner
			double s4 = u*v;					//邻近整数点(j1,i1)函数值的系数（右下角）right-down corner
 
			if((jz >=0) && (jz < h) && (iz >= 0) && (iz < w))
			{
				*(newImg+ey*zoomLineByte+ex) = *(temp+j1*originalLineByte+i1)*s1
					+*(temp+j1*originalLineByte+i2)*s3
					+*(temp+j2*originalLineByte+i1)*s2
					+*(temp+j2*originalLineByte+i2)*s4;
				}
				else
				{
					*(newImg+ey*zoomLineByte+ex) = 255;
				}
			dstImg[ey][ex]=newImg[ey*zoomLineByte+ex];
		}
	}
}
