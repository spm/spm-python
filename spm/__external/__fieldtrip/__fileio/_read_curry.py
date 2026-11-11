from spm._runtime import Runtime


def _read_curry(*args, **kwargs):
    r"""
      READ_CURRY reads and parses Curry V2 and V4 ascii files and returns the  
        content in a structure that is similar to the block-structured layout of  
        the file. This function does not interpret the content of the file, but  
        is intended as a helper function for READ_CURRY_XXX functions (where XXX  
        is the extension of the file).  
         
        Use as  
          s = read_curry(filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_curry.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_curry", *args, **kwargs)
