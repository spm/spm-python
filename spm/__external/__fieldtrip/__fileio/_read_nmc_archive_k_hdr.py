from spm._runtime import Runtime


def _read_nmc_archive_k_hdr(*args, **kwargs):
    r"""
      READ_NMC_ARCHIVE_K_HDR extracts 'header-data' for nmc_archive_k datasets  
         
        Use as  
          hdr = read_nmc_archive_k_hdr(paramfile)  
         
         
        This function specifically only reads data from one of the archived  
        datasets of the Neurophysiological Mechanisms of Cognition group of  
        Eric Maris, at the Donders Centre for Cognition, Radboud University,  
        Nijmegen, the Netherlands. It should not be used for any other data  
        format.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_nmc_archive_k_hdr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_nmc_archive_k_hdr", *args, **kwargs)
