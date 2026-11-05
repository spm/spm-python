from spm._runtime import Runtime


def _fiff_open_le(*args, **kwargs):
    r"""
       
        [fid, tree, dir] = fiff_open_le(fname)  
         
        Open a fif file and provide the directory of tags  
         
        fid     the opened file id  
        tree    tag directory organized into a tree  
        dir     the sequential tag directory  
         
        This is a modified version, specific for opening 'little endian' fiff files  
        Arjen Stolk  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/fiff_open_le.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_open_le", *args, **kwargs)
