#include <dlfcn.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>

uid_t setresuid( void ) {
	printf("Setting GUID");
        return 0;
}
/*

uid_t geteuid( void ) {
        return 1005;
}*/
