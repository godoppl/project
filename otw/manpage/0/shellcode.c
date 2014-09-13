#include <unistd.h>

void main(void) {
execl("/bin/cat", "/bin/cat",  "/etc/manpage_pass/manpage1", NULL);
}
