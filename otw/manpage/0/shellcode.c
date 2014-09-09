#include <unistd.h>

int main() {
	char *args[] = {"/bin/cat", "/etc/manpage_pass/manpage1", NULL};
	execv(args[0], args);
	return 0;
}
