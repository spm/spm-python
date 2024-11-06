from spm.__wrapper__ import Runtime


def _ft_getpos(*args, **kwargs):
    """
      Compute the inputs to TSSS code from Fieldtrip representation of MEG  
        sensors and headshape.  
       _______________________________________________________________________  
        Copyright (C) 2017  Vladimir Litvak based on MNE code by Matti Hamalainen  
        and Eric Larson  
         
        Redistribution and use of the Software in source and binary forms, with or without   
        modification, are permitted for non-commercial use.  
          
        The Software is provided "as is" without warranties of any kind, either express or  
        implied including, without limitation, warranties that the Software is free of defects,  
        merchantable, fit for a particular purpose. Developer/user agrees to bear the entire risk   
        in connection with its use and distribution of any and all parts of the Software under this license.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/TSSS/private/ft_getpos.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_getpos", *args, **kwargs)
