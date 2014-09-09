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
		ptrace(PTRACE_TRACEME, 0 , NULL, NULL);
		execl("/games/semtex/semtex4", "semtex4", NULL);
	}
	else {
		struct user_regs_struct regs;
		long orig_eax;
		int status;
		while(1) {
			waitpid(child, &status, 0);
			if(WIFEXITED(status)) break;
			long ret = ptrace (PTRACE_GETREGS, child, NULL, &regs);
			if (regs.orig_eax == __NR_geteuid || regs.orig_eax == __NR_geteuid32) {
				printf("Child made system call %03x\n", (unsigned int)regs.orig_eax);
				printf("eax = %08x ebx = %08x ecx = %08x edx = %08x\n", (unsigned int)regs.eax, (unsigned int)regs.ebx, (unsigned int)regs.ecx, (unsigned int)regs.edx);
				regs.eax = 6005;
				ret = ptrace(PTRACE_SETREGS, child, NULL, &regs);
			}
			ptrace(PTRACE_SYSCALL, child, NULL, NULL);
		}
	}
	return 0;
}

