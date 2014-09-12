#include <dlfcn.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>

uid_t getuid( void ) {
	printf("Checking GUID");
        return 1005;
}
/*

uid_t geteuid( void ) {
        return 1005;
}*/
