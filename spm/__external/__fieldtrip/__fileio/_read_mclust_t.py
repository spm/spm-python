from spm.__wrapper__ import Runtime


def _read_mclust_t(*args, **kwargs):
    """
      adapted from M-clust function LoadSpikes  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_mclust_t.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_mclust_t", *args, **kwargs)
