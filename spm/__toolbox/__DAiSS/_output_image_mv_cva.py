from spm.__wrapper__ import Runtime


def _output_image_mv_cva(*args, **kwargs):
    """
      cva code to plug into bf_output_image_mv function  
       function [chi,cva,t_stat] = bf_output_image_mv_cva(X,Y,c,U)  
        CVA. See Chatfield and Collins  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/output_image_mv_cva.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("output_image_mv_cva", *args, **kwargs)
