import os.path
import sys
import logging
import logging.handlers
import traceback
import fcntl
import array

CM_USB_Plug_IN = 108

root_path = '/'
user_path = '/root'
log_basepath = '/var/log'
flash_path = '/mnt/onboard'
ntx_io_path = '/dev/ntx_io'

installer_name = 'kobo_installer'
pack_name = 'packages'
installer_scripts_name = 'installer.d'

installer_path = os.path.join(user_path, installer_name)
pack_path = os.path.join(root_path, pack_name)
installer_scripts_path = os.path.join(root_path, installer_scripts_name)
installer_log_path = os.path.join(log_basepath, installer_name)
pack_db_path = os.path.join(installer_path, 'packinfo.sqlite')
reboot_path = os.path.join(installer_path, 'reboot')

def ioctl(f, signal, buffer_type):
    buf = array.array(buffer_type, [0])
    res = fcntl.ioctl(f, signal, buf)
    
    return res, buf

def usbIn():
    with open(ntx_io_path, mode='r+') as ntxf:
        isin = ioctl(ntxf, CM_USB_Plug_IN, 'i')[1]
    
    if isin:
        return True
    
    return False

def isLogDirEmpty(path):
    names = os.listdir(path)
    res = False
    
    for name in names:
        sub_path = os.path.join(path, name)
        
        if os.path.isdir(sub_path):
            if isLogDirEmpty(sub_path):
                res = True
        elif os.path.isfile(sub_path):
            if os.path.getsize(sub_path):
                res = True
            else:
                os.remove(sub_path)
        
    return False

class KoboDebugger():
    # Attributes:
    # 
    # str log_path
    # logging.Logger logger
    # float log_start
    
    def __init__(self, log_path, stream=None):
        logger = logging.getLogger()
        logger.setLevel(logging.WARNING)
        # for unix only
        fileh = logging.handlers.WatchedFileHandler(log_path, mode='a', 
                                                    delay=True)
        fileh.setLevel(logging.ERROR)
        streamh = logging.StreamHandler(stream)
        streamh.setLevel(logging.DEBUG)
        fmtstr = 'In {filename}, {levelname}: {message}'
        formatter = logging.Formatter(fmt=fmtstr, style='{')
        fileh.setFormatter(formatter)
        streamh.setFormatter(formatter)
        logger.addHandler(fileh)
        logger.addHandler(streamh)
        
        sys.excepthook = self.excHook
        
        self.logger = logger
        self.log_path = log_path
        
    def excHook(self, exc_type, exc_value, exc_tb):
        err_tpl = '''
Uncaught exception:
{0}
{1}: {2}'''
        err_str = err_tpl.format(''.join(traceback.format_tb(exc_tb)), 
                                 exc_type.__name__, 
                                 exc_value)
        self.logger.critical(err_str)

