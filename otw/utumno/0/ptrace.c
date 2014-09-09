#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/user.h>
#include <sys/syscall.h>
#include <unistd.h>

int main()
{   pid_t child;
    const int long_size = sizeof(long);
    child = fork();
    if(child == 0) {
        ptrace(PTRACE_TRACEME, 0, NULL, NULL);
        execl("/utumno/utumno0", "/utumno/utumno0", NULL, NULL, NULL);
    }
    else {
        int status;
        union u {
            long val;
            char chars[long_size];
        }data;
        struct user_regs_struct regs;
        int start = 0;
        long ins;
        while(1) {
            wait(&status);
            if(WIFEXITED(status))
                break;
            ptrace(PTRACE_GETREGS,
                   child, NULL, &regs);

            ins = ptrace(PTRACE_PEEKTEXT,
                             child, regs.rip,
                             NULL);
	    if(regs.rip < 09000000) {
            printf("EIP: %lx Instruction "
                  "executed: %lx\n",
                  regs.rip, ins);
	    }
	    else {
            ptrace(PTRACE_SINGLESTEP, child,
                      NULL, NULL);
	    }
        }
    }
    return 0;
}
