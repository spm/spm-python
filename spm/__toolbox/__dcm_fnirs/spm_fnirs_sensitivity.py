from spm.__wrapper__ import Runtime


def spm_fnirs_sensitivity(*args, **kwargs):
    """
      Calculate sensitivity matrix which corresponds to the effective  
        pathlength of detected photons for the channel measurements in the  
        hemodynamic source.   
        FORMAT [A] = spm_fnirs_sensitivity(DCM)  
          
        DCM - DCM structure or its filename  
         
        A - sensitivity matrix   
          
        Green's function (see \dcm_fnirs\mmclab\estimate_greens_mmclab.m)  
       --------------------------------------------------------------------------  
        G.s - estimated Green's function from sensor (light emitter) positions  
        into source positions [# sensor x # voxels x # wavelengths]   
        G.d - estimated Green's function from sensor (light detector) positions  
        into source positions [# sensor x # voxels x # wavelengths]   
        G.xyz - MNI locations [3 x # voxels]   
        G.elem - tissue types of voxels [3 x # voxels]   
        1-scalp, 2-CSF, 3-gray matter, 4-white matter   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_fnirs_sensitivity.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fnirs_sensitivity", *args, **kwargs)
