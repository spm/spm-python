from spm.__wrapper__ import Runtime


def _hcp_provenance(*args, **kwargs):
    """
      HCP_PROVENANCE returns a structure with provenance information  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/hcp_provenance.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("hcp_provenance", *args, **kwargs)
