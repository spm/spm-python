from spm._runtime import Runtime


def _read_imotions_txt(*args, **kwargs):
    r"""
      READ_IMOTIONS_TXT reads *.txt files that are exported from the iMotions software.  
         
        Use as  
          dat = read_imotions_txt(filename  
         
        See also TEXTSCAN  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/read_imotions_txt.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_imotions_txt", *args, **kwargs)
