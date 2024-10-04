from spm.__wrap__ import _Runtime


def _output_image_mv_cva(*args, **kwargs):
  """  cva code to plug into bf_output_image_mv function  
   function [chi,cva,t_stat] = bf_output_image_mv_cva(X,Y,c,U)  
    CVA. See Chatfield and Collins  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/output_image_mv_cva.m)
  """

  return _Runtime.call("output_image_mv_cva", *args, **kwargs)
