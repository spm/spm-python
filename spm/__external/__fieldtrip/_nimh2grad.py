from spm.__wrapper__ import Runtime


def _nimh2grad(*args, **kwargs):
    """
      NIMH2GRAD constructs a gradiometer definition from the res4 header whish  
        is read using the NIMH implementation of ctf_read_res4. The grad  
        structure is compatible with FieldTrip and Robert Oostenveld's low-level  
        forward and inverse routines.  
         
        Use as  
          hdr  = ctf_read_res4(dataset);  
          grad = nimh2grad(hdr;  
         
        See also CTF2GRAD, FIF2GRAD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/nimh2grad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("nimh2grad", *args, **kwargs)
