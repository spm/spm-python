from spm.__wrapper__ import Runtime


def bemcp_example(*args, **kwargs):
    """
      Simple function to test/demonstrate how the Boundary element functions are  
        used in combination with Fildtrip/Forwinv routines.  
         
        1. A model is created as 3 concentric meshed spheres (using FT's   
        icosahedron routines),   
        2. then random electrodes are placed on the upper part of the outer   
        sphere.   
        3. the model is then "prepared" with 'ft_prepare_bemmodel', this bits  
        takes most time as it requires LOTS of calculation.  
        4. sensors and volumes are plugged together by 'forwinv_prepare_vol_sens'  
        5. Finally the leadfiled for 3 orthogonal sources placed at one location  
        is calculated with 'forwinv_compute_leadfield.m'  
        6. Display the 3 leadfields  
         
        NOTE:   
        this bit of code needs access to low level fieldtrip/forwinv routines   
        which have been copy/pasted here under.  
        Be aware that this way of programming is generally NOT advisable!  
        I used it only to ensure a quick & dirty check of the BEM module...  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/bemcp/bemcp_example.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bemcp_example", *args, **kwargs, nargout=0)
