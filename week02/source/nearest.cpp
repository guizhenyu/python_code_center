//nearest interpolation method for resize(zoom)
void onNearest(CDib &m_Dib, BYTE **srcImg,BYTE **dstImg,int h,int w,double zoomNumber)
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
		for(ex = 0; ex < zoomLineByte;ex++)
		{
			j = (int)(ey/zoomNumber + 0.5); //nearest value
			i = (int)(ex/zoomNumber + 0.5);
			if((i >= 0) && (i < w) && (j >= 0)&& (j < h))
			{	
				 //memcpy(&newImg[ey * zoomLineByte] + ex * m_Dib.GetBitCount() / 8,&temp[j * originalLineByte] + i * m_Dib.GetBitCount() <span style="white-space:pre">				</span> //<span style="white-space:pre">			</span>/ 8,m_Dib.GetBitCount() / 8); 			
				newImg[ey*zoomLineByte+ex] = temp[j*originalLineByte+i];
			}
			else
			{
				newImg[ey*zoomLineByte+ex] = 255;
			}
			dstImg[ey][ex]=newImg[ey*zoomLineByte+ex];
		}
	}
}
