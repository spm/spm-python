from spm._runtime import Runtime


def _read_mclust_t(*args, **kwargs):
    r"""
      adapted from M-clust function LoadSpikes  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_mclust_t.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_mclust_t", *args, **kwargs)
