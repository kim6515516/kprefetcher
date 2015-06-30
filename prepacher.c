int main(void) { 
	posix_fadvise(50,0,40960 );
	posix_fadvise(40,1024,30000 );
	return 0;
}