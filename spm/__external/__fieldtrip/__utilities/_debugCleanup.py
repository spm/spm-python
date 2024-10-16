from spm.__wrapper__ import Runtime


def _debugCleanup(*args, **kwargs):
  """  DEBUGCLEANUP is a cleanup function that is being used by FT_PREAMBLE_DEBUG. It is  
    called when a high-level FieldTrip function exits, either after finishing successfully or after detecting an error.  
     
    See also FT_PREAMBLE_DEBUG, FT_POSTAMBLE_DEBUG  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/debugCleanup.m)
  """

  return Runtime.call("debugCleanup", *args, **kwargs, nargout=0)
