from spm._runtime import Runtime


def _read_caret_spec(*args, **kwargs):
    r"""
      READ_CARET_SPEC reads in a caret .spec file.  
         
        Use as  
          [spec, headerinfo] = read_caret_spec(specfile)  
         
        Output arguments:  
          spec       = structure containing per file type the files listed  
          headerinfo = structure containing the specfile header  
         
        The file can be an xml-file or an ascii formatted file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_caret_spec.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_caret_spec", *args, **kwargs)
