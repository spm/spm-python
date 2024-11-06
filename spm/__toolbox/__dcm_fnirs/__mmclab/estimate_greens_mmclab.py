from spm.__wrapper__ import Runtime


def estimate_greens_mmclab(*args, **kwargs):
    """
      Estimate Green's function of the photon fluence by simulating photon  
        migration through the head and brain using the MMCLAB software  
         
        This function provides input parameters to perform the Monte Carlo  
        simulation. Output of MMCLAB, Green's function, is then saved as data  
        format to be used in DCM-fNIRS analysis.   
          
        Following software and Brain atlas are required:   
        MMCLAB: http://mcx.sourceforge.net/cgi-bin/index.cgi?MMC/Doc/MMCLAB  
        iso2mesh: http://iso2mesh.sourceforge.net/cgi-bin/index.cgi  
        Brain atlas mesh: http://mcx.sourceforge.net/cgi-bin/index.cgi?MMC/Colin27AtlasMesh  
        Collin 27 average brain: http://www.bic.mni.mcgill.ca/ServicesAtlases/Colin27  
         
        FORMAT [G] = estimate_greens_mmclab(F, P)   
         
        G                 Green's function of the photon fluence   
         
        F                  names of files required to use MMClab software  
        P                  optical parameters for Monte Carlo simulation  
         
       --------------------------------------------------------------------------  
        F.mmc          name of directory of MMCLAB (eg, /mmclab)  
        F.isomesh     name of directory of iso2mesh (eg, /iso2mesh)  
        F.mesh         file name of brain atlas mesh (eg, MMC_Collins_Atlas_Mesh_Version_2L.mat)  
        F.atlas         file name of Collin 27 brain (eg, colin27_t1_tal_lin.nii)   
        F.sdpos        file name of MNI locations of optical source and detectors   
                            If F is not specified, files are selected using GUI.   
       --------------------------------------------------------------------------  
        P                  optical parameters for Monte Carlo simulation  
                            if this is not specified, optical parameters for 750  
                            nm and 850 nm are used.   
       --------------------------------------------------------------------------  
        G.s - estimated Green's function from sensor (light emitter) positions  
        into source positions [# sensor x # voxels x # wavelengths]   
        G.d - estimated Green's function from sensor (light detector) positions  
        into source positions [# sensor x # voxels x # wavelengths]   
        G.xyz - MNI locations [3 x # voxels]   
        G.elem - tissue types of voxels [3 x # voxels]   
        1-scalp, 2-CSF, 3-gray matter, 4-white matter   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/mmclab/estimate_greens_mmclab.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("estimate_greens_mmclab", *args, **kwargs)
