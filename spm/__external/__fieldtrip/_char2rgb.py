from spm._runtime import Runtime


def _char2rgb(*args, **kwargs):
    """
      CHAR2RGB converts the line color character into the corresponding RGB triplet  
         
        see https://nl.mathworks.com/help/matlab/ref/colorspec.html  
        and https://nl.mathworks.com/matlabcentral/fileexchange/48155-convert-between-rgb-and-color-names  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/char2rgb.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("char2rgb", *args, **kwargs)
