from mpython import Runtime


def _hcp_provenance(*args, **kwargs):
    """
      HCP_PROVENANCE returns a structure with provenance information


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/hcp_provenance.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("hcp_provenance", *args, **kwargs)
