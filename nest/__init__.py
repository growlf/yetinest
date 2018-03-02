from fabric.api import prompt, env, local


def get_image():
    """Download a fresh OS image if one is not already available"""

    ####TODO: check to see if we already HAVE the image before downloading
    result = local('wget https://oph.mdrjr.net/meveric/images/Jessie/Debian-Jessie-1.1.4-20171121-XU3+XU4.img.xz')
    return result


# Write the OS image to the card
def write_image():
    """Burn the OS image to the selected device"""

    prompt('What device do you want to burn the node images to? (MAKE SURE YOU KNOW WHICH DEVICE IS THE CORRECT ONE!!)', 'target_device', default='mmcblk1')

    result = local("xzcat Debian-Jessie-1.1.4-20171121-XU3+XU4.img.xz | sudo dd of=%s status='progress'" % env.target_device)

    return result

