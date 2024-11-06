from spm.__wrapper__ import Runtime


def _read_curry(*args, **kwargs):
    """
      READ_CURRY reads and parses Curry V2 and V4 ascii files and returns the  
        content in a structure that is similar to the block-structured layout of  
        the file. This function does not interpret the content of the file, but  
        is intended as a helper function for READ_CURRY_XXX functions (where XXX  
        is the extension of the file).  
         
        Use as  
          s = read_curry(filename)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_curry.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_curry", *args, **kwargs)
