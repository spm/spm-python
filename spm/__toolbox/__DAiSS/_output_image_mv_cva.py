from spm._runtime import Runtime


def _output_image_mv_cva(*args, **kwargs):
    r"""
      cva code to plug into bf_output_image_mv function  
       function [chi,cva,t_stat] = bf_output_image_mv_cva(X,Y,c,U)  
        CVA. See Chatfield and Collins  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/private/output_image_mv_cva.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("output_image_mv_cva", *args, **kwargs)
