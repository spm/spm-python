from spm.__wrap__ import _Runtime


def _write_neuralynx_ncs(*args, **kwargs):
  """  WRITE_NEURALYNX_NCS writes continuous data to a NCS file  
     
    Use as  
      write_neuralynx_ncs(filename, ncs)  
     
    The input data should be scaled in uV.  
     
    See also READ_NEURALYNX_NCS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_neuralynx_ncs.m)
  """

  return _Runtime.call("write_neuralynx_ncs", *args, **kwargs, nargout=0)
