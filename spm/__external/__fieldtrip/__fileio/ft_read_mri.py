from spm.__wrapper__ import Runtime


def ft_read_mri(*args, **kwargs):
    """
      FT_READ_MRI reads anatomical and functional MRI data from different file formats.  
        The output data is structured in such a way that it is compatible with  
        FT_DATATYPE_VOLUME.  
         
        Use as  
          [mri] = ft_read_mri(filename, ...)  
         
        Additional options should be specified in key-value pairs and can include  
          'dataformat'  = string specifying the file format, determining the low-level  
                          reading routine to be used. If no explicit format is given,  
                          it is determined automatically from the filename.  
          'volumes'     = vector with the volume indices to read from a 4D nifti (only for 'nifti_spm')  
          'outputfield' = string specifying the name of the field in the structure in which the  
                          numeric data is stored (default = 'anatomy')  
          'fixel2voxel' = string, the operation to apply to the fixels belonging to the  
                          same voxel, can be 'max', 'min', 'mean' (only for 'mrtrix_mif', default = 'max')  
          'indexfile'   = string, pointing to a fixel index file, if not present in the same directory  
                          as the functional data (only for 'mrtrix_mif')  
          'spmversion'  = string, version of SPM to be used (default = 'spm12')  
          'readbids'    = string, 'yes', no', or 'ifmakessense', whether to read information from  
                          the BIDS sidecar files (default = 'ifmakessense')  
         
        The supported dataformats are  
          'afni_head'/'afni_brik'      uses AFNI code  
          'analyze_img'/'analyze_hdr'  uses SPM code  
          'analyze_old'                uses Darren Webber's code  
          'asa_mri'  
          'ctf_mri'  
          'ctf_mri4'  
          'ctf_svl'  
          'dicom'                      uses SPM code, same as dicom_spm  
          'dicom_spm'                  uses SPM code, also allows for multiframe dicoms (one volume in a file)       
          'dicom_fs'                   uses FreeSurfer code, which relies on MATLAB image processing toolbox  
          'dicom_old'                  uses MATLAB image processing toolbox code  
          'freesurfer_mgh'             uses FreeSurfer code  
          'freesurfer_mgz'             uses FreeSurfer code  
          'jnifti_jnii'  
          'jnifti_bnii'  
          'matlab'                     assumes a MATLAB *.mat file containing a struct  
          'minc'                       uses SPM, this requires SPM5 or older  
          'mrtrix_mif'                 uses mrtrix code  
          'neuromag_fif'               uses MNE toolbox code  
          'neuromag_fif_old'           uses meg-pd toolbox  
          'nifti'                      uses FreeSurfer code  
          'nifti_spm'                  uses SPM code  
          'seg3d_mat'                  MATLAB file from Seg3D with a scirunnrrd structure  
          'yokogawa_mri'  
         
        The following MRI file formats are supported  
          AFNI (*.head, *.brik)  
          ANT - Advanced Neuro Technology (*.mri)  
          Analyze (*.img, *.hdr)  
          CTF (*.svl, *.mri version 4 and 5)  
          DICOM (*.dcm, *.ima)  
          FreeSurfer (*.mgz, *.mgh)  
          MATLAB (*.mat)  
          MINC (*.mnc)  
          Mrtrix image format (*.mif)  
          NIFTi (*.nii) and zipped NIFTi (*.nii.gz)  
          Neuromag/Elekta/Megin (*.fif)  
          Yokogawa (*.mrk, incomplete)  
         
        If you have a series of DICOM files, please provide the name of any of the files in  
        the series (e.g. the first one). The files corresponding to the whole volume will  
        be found automatically.  
         
        The output MRI may have a homogenous transformation matrix that converts the  
        coordinates of each voxel (in xgrid/ygrid/zgrid) into head coordinates.  
         
        If the input file is a 4D nifti, and you wish to load in just a subset of the  
        volumes, for example due to memory constraints, you should use as dataformat 'nifti_spm',  
        which uses the optional key-value pair 'volumes' = vector, with the indices of the  
        to-be-read volumes. The order of the indices is ignored, and the volumes will be  
        sorted according to the original numeric indices, i.e., 1:10 yields the same as 10:-1:1  
         
        See also FT_DATATYPE_VOLUME, FT_WRITE_MRI, FT_READ_DATA, FT_READ_HEADER, FT_READ_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_mri.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_read_mri", *args, **kwargs)
