from spm._runtime import Runtime


def _hcp_provenance(*args, **kwargs):
    r"""
      HCP_PROVENANCE returns a structure with provenance information  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/hcp_provenance.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("hcp_provenance", *args, **kwargs)
