#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>


int main(void) { 

	int fd0 = open("eventfd", 'r');
	posix_fadvise(fd0, 0, 16, POSIX_FADV_NOREUSE);
	posix_fadvise(fd0,0,32, POSIX_FADV_NOREUSE);

	int fd1 = open("iozone.tmp", 'r');
	posix_fadvise(fd1, 262144, 0, POSIX_FADV_NOREUSE);
	posix_fadvise(fd1,262144,0, POSIX_FADV_NOREUSE);
	posix_fadvise(fd1,262144,262144, POSIX_FADV_NOREUSE);
	posix_fadvise(fd1,262144,524288, POSIX_FADV_NOREUSE);
	posix_fadvise(fd1,262144,786432, POSIX_FADV_NOREUSE);
	posix_fadvise(fd1,262144,0, POSIX_FADV_NOREUSE);
	posix_fadvise(fd1,262144,0, POSIX_FADV_NOREUSE);
	posix_fadvise(fd1,262144,262144, POSIX_FADV_NOREUSE);
	posix_fadvise(fd1,262144,524288, POSIX_FADV_NOREUSE);
	posix_fadvise(fd1,262144,786432, POSIX_FADV_NOREUSE);


	close(fd0);
	close(fd1);
	return 0;
}