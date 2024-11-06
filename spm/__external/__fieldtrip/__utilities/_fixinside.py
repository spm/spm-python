from spm.__wrapper__ import Runtime


def _fixinside(*args, **kwargs):
    """
      FIXINSIDE ensures that the region of interest (which is indicated by the  
        field "inside") is consistently defined for source structures and volume  
        structures. Furthermore, it solves backward compatibility problems.  
         
        Use as  
          [source] = fixinside(source, 'logical');  
        or  
          [source] = fixinside(source, 'index');  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/fixinside.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fixinside", *args, **kwargs)
