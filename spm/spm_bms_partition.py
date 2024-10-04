from spm.__wrap__ import _Runtime


def spm_bms_partition(*args, **kwargs):
  """  Compute model partitioning for BMS  
    FORMAT spm_bms_partition(BMS)  
     
    Input:  
    BMS structure (BMS.mat)  
     
    Output:  
    PPM (images) for each of the subsets defined  
    xppm_subsetn.img (RFX) and ppm_subsetn.img (FFX)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_bms_partition.m)
  """

  return _Runtime.call("spm_bms_partition", *args, **kwargs, nargout=0)
