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
                execl("/maze/maze0", "maze0", NULL);
        }
        else {
		int status;
		struct user_regs_struct regs;
//		long orig_eax;
//		long uidpoint;
		long addr;
//		long oldret = 0;
		while (1){
		waitpid(child, &status, 0);
		if(WIFEXITED(status)) break;
		long regis = ptrace(PTRACE_GETREGS, child, NULL, &regs);
//		addr = regs.esp;
//		long ret = ptrace(PTRACE_PEEKDATA, child, addr, NULL);
		if (regs.eax == 0x3a99 || regs.eax == 0x3a98) {
			printf("EAX is %d", (unsigned int)regs.eax);
//			ptrace(PTRACE_POKEDATA, child, addr, 0x3ed);
/			ptrace(PTRACE_SYSCALL, child, NULL, NULL);
			}
//		else{
//			printf("eax:%08x, ebx:%08x, ecx:%08x, edx:%08x, esp:%08x, ebp:%08x\n", (unsigned int)regs.eax, (unsigned int)regs.ebx, (unsigned int)regs.ecx, (unsigned int)regs.edx, (unsigned int)regs.esp, (unsigned int)regs.ebp);
		ptrace(PTRACE_SYSCALL, child, NULL, NULL);
//			}
		}
		                
        }
        return 0;
}


