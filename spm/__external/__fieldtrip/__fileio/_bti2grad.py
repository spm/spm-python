from spm.__wrapper__ import Runtime


def _bti2grad(*args, **kwargs):
    """
      BTI2GRAD converts a 4D header to a gradiometer structure that can be  
        understood by FieldTrip and Robert Oostenveld's low-level forward and  
        inverse routines. This function only works for headers that have been  
        read using the READ_4D_HDR function.  
         
        Use as:  
          [hdr]  = read_4d_hdr(filename)  
          [grad] = bti2grad(hdr)  
         
        or  
         
          [hdr]  = read_4d_hdr(filename)  
          [grad, elec] = bti2grad(hdr)  
         
        This function only computes the hardware magnetometer definition  
        for the 4D system. This function is based on ctf2grad and Gavin  
        Paterson's code, which was adapted from Eugene Kronberg's code  
         
        See also CTF2GRAD, FIF2GRAD, MNE2GRAD, ITAB2GRAD, YOKOGAWA2GRAD,  
        FT_READ_SENS, FT_READ_HEADER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/bti2grad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bti2grad", *args, **kwargs)
