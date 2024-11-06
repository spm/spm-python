from spm.__wrapper__ import Runtime


def spm_fx_bgt(*args, **kwargs):
    """
      State equations for a neural mass model of the basal ganglia & thalamus  
        [striatum, gpe, stn, gpi, and thalamus] as a  
        single source (no extrinsic connections)  
         
        order           cells     states  
        1 = striatum  - ii        x(1,1:2)  
        2 = gpe       - ii        x(1,3:4)  
        3 = stn       - pyr       x(1,5:6)  
        4 = gpi       - ii        x(1,7:8)  
        5 = thalamus  - pyr       x(1,9:10)  
         
        G(1,1) = str -> str (-ve self)  
        G(1,2) = str -> gpe (-ve ext)  
        G(1,3) = gpe -> gpe (-ve self)  
        G(1,4) = gpe -> stn (-ve ext)  
        G(1,5) = stn -> gpe (+ve ext)  
        G(1,6) = str -> gpi (-ve ext)  
        G(1,7) = stn -> gpi (+ve ext)  
        G(1,8) = gpi -> gpi (-ve self)  
        G(1,9) = gpi -> tha (-ve ext)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_bgt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_bgt", *args, **kwargs)
