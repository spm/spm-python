from spm._runtime import Runtime


def ft_read_json(*args, **kwargs):
    r"""
      FT_READ_JSON reads information from a JSON file and represents it as a MATLAB structure  
         
        Use as  
          json = ft_read_json(filename)  
         
        See also FT_WRITE_JSON, FT_READ_TSV, FT_WRITE_TSV, JSONDECODE, JSONENCODE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/ft_read_json.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_read_json", *args, **kwargs)
