#! /usr/bin/python2.7
import subprocess

print("============================================")
#pipeCliCmds = (['grep', 'crw'], ['grep', 'nvme'])
pipeCliCmds = (['ls', '-la'], ['ls', '-la'])
subPipe=[]
for cliCmd in pipeCliCmds:
    print(cliCmd)
    #subPipe.append(list(cliCmd))
    #print(subPipe)
    #pro = subprocess.Popen(subPipe)
    pro = subprocess.Popen(cliCmd)
    pro.wait()
del pro

print("============================================")
class CLICommand(list):
    def __init__(self):
        DEBUG_MSG('KK_ [class CLICommand(list)][__init__]', color=DEBUG.Color.RED)
        self.stdout=''
        self.stderr=''

class ToolKit(CLICommand):
    def __init__(self, path=".\\general", exe=None, **common):
        '''
        Base Class for tool kit, provide 4 type of issue API
        issue           : direct issue  , ie : [self.prefix] self._exe [parameters] [self.suffix]
        issue_ex        : piple issue   , ie : [self.prefix] self._exe [parameters] | piple1 cli | piple2 cli ...
        issue_redirect  : redirect issue, ie : [self.prefix] self._exe [parameters] [self.suffix] > file
        system_call     : system call   , ie : os.system([self.prefix] self._exe [parameters] [self.suffix])
        Notice : prefix and suffix append if they are not None
        '''
        DEBUG_MSG('KK_ [class ToolKit(CLICommand)][__init__]', color=DEBUG.Color.RED)
        super(ToolKit, self).__init__()
        self._path          =path
        self._exe           =exe
        self.suffix         =None
        self.prefix         =None
        self.__common       =common
        self.__lastLatency   =0

def _device_list(self):
    from tools.tool_kit import ToolKit, CLICommand
    DEBUG_MSG('KK_ [class NVMeCli(NVMeCmdTool)][_device_list]', color=DEBUG.Color.RED)
    ls = ToolKit(path='', exe='ls')
    grep1 = CLICommand()
    grep2 = CLICommand()

    ls << '-al' << '/dev'
    grep1 << 'grep' << 'crw'
    grep2 << 'grep' << 'nvme'
    pipeCliCmds = [grep1, grep2]  #
    DEBUG_MSG('KK_ [class NVMeCli(NVMeCmdTool)][_device_list] - pipeCliCmds=%s' % pipeCliCmds)
    ls.issue_ex(pipeCliCmds=pipeCliCmds)
    del pipeCliCmds[:]

    lines = ls.stdout.split('\n')
    del self._numlist[:]
    for line in lines:
        if line.startswith('crw'):
            num = eval(line.split('nvme')[-1])
            self._numlist.append(num)

    DEBUG_MSG('Device List : %s' % self._numlist)
    rst = len(self._numlist)
    DEBUG_MSG('KK_ [class NVMeCli(NVMeCmdTool)][_device_list] - rst = %d' % rst)
    return rst

'''
    def issue_ex(self, pipeCliCmds, addPath=False):
        if addPath:
            cli=str(CrossPlatform.Folder(self._path)+self._exe)
        else:
            cli=self._exe
        self._common_argus_before_issue(**self.__common)
        if self.prefix is not None:
            cli=self.prefix+' '+cli
        mainCmd=[]
        mainCmd.append(cli)
        mainCmd.extend(list(self))
        DEBUG_MSG('KK_ [class ToolKit(CLICommand)][issue_ex] - mainCmd=%s' % mainCmd, color=DEBUG.Color.MAGENTA)
        #print(mainCmd)
        #if self.suffix:
        #    pipeList.append(self.suffix)
        subPipe=[]
        for cliCmd in pipeCliCmds:
            subPipe.append(list(cliCmd))
        while not self.__toolKitLocker.acquire(False): time.sleep(0.1)
        lt=time.time()
        if CrossPlatform.is_windows():
            #proc = subprocess.Popen(pipeList, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
            proc = subprocess.Popen(mainCmd, stdout=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
            #proc = subprocess.Popen(pipeList, stdout=subprocess.PIPE, shell=True)
        elif CrossPlatform.is_linux():
            proc = subprocess.Popen(' '.join(mainCmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            #proc = subprocess.Popen(mainCmd, stdout=subprocess.PIPE, shell=False)
        procMain=proc
        for sub in subPipe:
            #proc = subprocess.Popen(sub,stdin=proc.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            proc = subprocess.Popen(sub,stdin=proc.stdout, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            DEBUG_MSG('KK_ [class ToolKit(CLICommand)][issue_ex] - sub=%s' % sub,  color=DEBUG.Color.MAGENTA)
            #print(sub)

        procMain.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
        self.__toolKitLocker.release()

        self.stdout, self.stderr=proc.communicate()

        lt=time.time()-lt
        self.__lastLatency = lt * 10 ** 6
        rst = procMain.returncode
        self._purge_cli_command()
        return self.__rst_post(rst)
'''
