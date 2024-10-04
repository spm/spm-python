from spm.__wrap__ import _Runtime


def _hcp_provenance(*args, **kwargs):
  """  HCP_PROVENANCE returns a structure with provenance information  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/hcp_provenance.m)
  """

  return _Runtime.call("hcp_provenance", *args, **kwargs)
