import subprocess
device = ['a51', 'm31s', 'f41', 'm31', 'm21']
rom = ['aosp', 'oneui']
ksu = ['', '--no-ksu']


for devices in device:
    for rom_def in rom:
        for ksu_suport in ksu:
            sub = subprocess.Popen(['python', 'build_kernel.py', '--target', devices, '--' + rom_def, ksu_suport], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = sub.communicate()
            print(out.decode('utf-8'))
            print(err.decode('utf-8'))