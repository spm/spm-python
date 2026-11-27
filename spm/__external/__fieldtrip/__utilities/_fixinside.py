from spm._runtime import Runtime


def _fixinside(*args, **kwargs):
    r"""
      FIXINSIDE ensures that the region of interest (which is indicated by the  
        field "inside") is consistently defined for source structures and volume  
        structures. Furthermore, it solves backward compatibility problems.  
         
        Use as  
          [source] = fixinside(source, 'logical');  
        or  
          [source] = fixinside(source, 'index');  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/fixinside.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixinside", *args, **kwargs)
