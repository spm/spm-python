from spm.__wrapper__ import Runtime


def _warp_fsaverage(*args, **kwargs):
    """
      WARP_FSAVERAGE maps electrodes onto FreeSurfer's fsaverage brain.  
        This surface-based registration technique solely considers the curvature  
        patterns of the cortex and thus can be used for the spatial normalization  
        of electrodes located on or near the cortical surface. To perform  
        surface-based normalization, you first need to process the subject's MRI  
        with FreeSurfer's recon-all functionality.  
         
        The configuration must contain the following options  
          cfg.headshape      = string, filename containing subject headshape   
                             (e.g. <path to freesurfer/surf/lh.pial>)  
          cfg.fshome         = string, path to freesurfer  
         
        See also FT_ELECTRODEREALIGN, FT_PREPARE_MESH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/warp_fsaverage.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("warp_fsaverage", *args, **kwargs)
