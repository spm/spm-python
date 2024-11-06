from spm.__wrapper__ import Runtime


def spm_eeg_inv_ecd_DrawDip(*args, **kwargs):
    """
      Display the dipoles as obtained from VB-ECD  
        FORMAT spm_eeg_inv_ecd_DrawDip('Init',[sdip,[P]])  
        Display dipoles from SDIP structure on image P [Default is avg152T1]  
         
        If multiple seeds have been used, you can select the seeds to display   
        by pressing their index.   
        Given that the sources could have different locations, the slices  
        displayed will be the 3D view at the *average* or *mean* locations of  
        selected sources.  
        If more than 1 dipole was fitted at a time, then selection of source 1   
        to N is possible through the pull-down selector.  
         
        The location of the source/cut is displayed in mm and voxel, as well as  
        the underlying image intensity at that location.  
        The cross hair position can be hidden by clicking on its button.  
         
        Nota_1: If the cross hair is manually moved by clicking in the image or  
                changing its coordinates, the dipole displayed will NOT be at  
                the right displayed location...  
         
        Nota_2: Some seeds may have not converged within the limits fixed,  
                these dipoles are not displayed...  
         
        Fields needed in sdip structure to plot on an image:  
          n_seeds - number of seeds set used, i.e. number of solutions calculated  
          n_dip   - number of fitted dipoles on the EEG time series  
          loc     - location of fitted dipoles, cell{1,n_seeds}(3 x n_dip)  
                    remember that loc is fixed over the time window.  
          j       - sources amplitude over the time window,   
                    cell{1,n_seeds}(3*n_dip x Ntimebins)  
          Mtb     - index of maximum power in EEG time series used  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_eeg_inv_ecd_DrawDip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_ecd_DrawDip", *args, **kwargs, nargout=0)
