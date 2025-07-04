from spm._runtime import Runtime


def _volumeflip(*args, **kwargs):
    """
      VOLUMEFLIP  
         
        See also VOLUMEPERMUTE, ALIGN_IJK2XYZ, ALIGN_XYZ2IJK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/volumeflip.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumeflip", *args, **kwargs)
