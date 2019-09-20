float Calc(float x);
int _tmain(int atgc,_TCHAR* argv[])
{
	for(int i=0;i<=10;i++)
		count<<Calc((float)i)<<'\n';
	return 0;
}
float Calc(float a)
{
if(a<1e-6)
	return 0;

float x=a/2;
float t=a;
while(fabs(x-t)>1e-6)
	{t=x;+
	x=(x+a/x)/2;
	}
	return x;
}