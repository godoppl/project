#include <dlfcn.h>
#include <unistd.h>
#include <sys/types.h>

uid_t geteuid32( void ) {
        return 15001;
}


uid_t geteuid( void ) {
        return 15001;
}
