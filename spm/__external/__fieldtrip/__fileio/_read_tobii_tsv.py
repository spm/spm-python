from spm.__wrapper__ import Runtime


def _read_tobii_tsv(*args, **kwargs):
    """
      READ_TOBII_TSV  
         
        Use as  
          hdr = read_tobii_tsv(filename)  
        or  
          dat = read_tobii_tsv(filename, tsv, begsample, endsample)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tobii_tsv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_tobii_tsv", *args, **kwargs)
