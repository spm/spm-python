from spm.__wrapper__ import Runtime


def _read_caret_spec(*args, **kwargs):
    """
      READ_CARET_SPEC reads in a caret .spec file.  
         
        Use as  
          [spec, headerinfo] = read_caret_spec(specfile)  
         
        Output arguments:  
          spec       = structure containing per file type the files listed  
          headerinfo = structure containing the specfile header  
         
        The file can be an xml-file or an ascii formatted file  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_caret_spec.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_caret_spec", *args, **kwargs)
