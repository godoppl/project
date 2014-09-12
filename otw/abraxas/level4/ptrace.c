#include <unistd.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/user.h>
#include <stdio.h>
#include <asm/unistd_32.h>

int main(void) {
        pid_t child;
        child = fork();

        if(child == 0) {
                ptrace(PTRACE_ATTACH, 21793 , NULL, NULL);
//                execl("/home/level5/bin/fsas", "fsas", NULL);
        }
        else {
                struct user_regs_struct regs;
                long orig_eax;
		long position;
		long pos2;
		long pos3;
                int status;
                while(1) {
                        waitpid(child, &status, 0);
                        if(WIFEXITED(status)) break;
                        long ret = ptrace (PTRACE_GETREGS, child, NULL, &regs);
			if (regs.eax >= 0x0){
//                              printf("Child made system call %03x \n", (unsigned int)regs.eax);
				position = regs.esp;
				pos2 = regs.esp-0x4;
//				pos3 = position+0x14;
				long dat = ptrace(PTRACE_PEEKDATA, child, position, NULL);
				long dat2 = ptrace(PTRACE_PEEKDATA, child, pos2, NULL);
//				long dat3 = ptrace(PTRACE_PEEKDATA, child, pos3, NULL);
                                printf("ESP: %08x, dat: %08x, dat-0x4: %08x\n", (unsigned int)regs.esp, (unsigned int)dat, (unsigned int)dat2);
//                                dat3 = ptrace(PTRACE_POKEDATA, child, pos3, 0x7a69);
                        }
                        ptrace(PTRACE_SYSCALL, child, NULL, NULL);
                }
        }
        return 0;
}

