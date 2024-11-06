from spm.__wrapper__ import Runtime


def _volumepermute(*args, **kwargs):
    """
      VOLUMEPERMUTE  
         
        See also VOLUMEFLIP, ALIGN_IJK2XYZ, ALIGN_XYZ2IJK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/volumepermute.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("volumepermute", *args, **kwargs)
