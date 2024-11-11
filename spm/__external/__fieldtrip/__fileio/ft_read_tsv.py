from spm.__wrapper__ import Runtime


def ft_read_tsv(*args, **kwargs):
    """
      FT_READ_TSV reads information from a tab-separated-values file and represents it as a MATLAB table  
         
        Use as  
          tsv = ft_read_tsv(filename)  
         
        See also FT_WRITE_TSV, FT_READ_JSON, FT_WRITE_JSON, READTABLE, WRITETABLE, TDFREAD, TBLREAD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_tsv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_read_tsv", *args, **kwargs)
