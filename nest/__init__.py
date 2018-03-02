from fabric.api import prompt

################################################
#### Temp library scratchpad as we rapid-prototype this thingy-ma-bob
def set_targetdevice():
    prompt('What device do you want to burn the node images to? (MAKE SURE YOU KNOW WHICH DEVICE IS THE CORRECT ONE!!)', 'target_device', default='mmcblk1')
    print("/dev/%s" % env.target_device)
