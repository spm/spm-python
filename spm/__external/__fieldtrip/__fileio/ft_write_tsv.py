from spm._runtime import Runtime


def ft_write_tsv(*args, **kwargs):
    r"""
      FT_WRITE_TSV writes a MATLAB table to a tab-separated-values file. Compared to the  
        builtin MATLAB function, this implementation deals a bit different with missing  
        values, booleans, and NaNs.  
         
        Use as  
          ft_write_tsv(filename, table)  
         
        See also FT_READ_TSV, FT_READ_JSON, FT_WRITE_JSON, READTABLE, WRITETABLE, TBLWRITE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/ft_write_tsv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_write_tsv", *args, **kwargs, nargout=0)
