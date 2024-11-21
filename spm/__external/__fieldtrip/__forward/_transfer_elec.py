from spm.__wrapper__ import Runtime


def _transfer_elec(*args, **kwargs):
    """
      TRANSFER_ELEC is the transfermatrix from vertex to electrode potentials  
        using bi-linear interpolation over the triangles  
         
        tra = transfer_elec(pnt, tri, el)  
         
        the Nx3 matrix el shold contain [tri, la, mu] for each electrode  
         
        See also PROJECT_ELEC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/transfer_elec.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("transfer_elec", *args, **kwargs)
