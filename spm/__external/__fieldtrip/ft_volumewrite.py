from spm.__wrapper__ import Runtime


def ft_volumewrite(*args, **kwargs):
    """
      FT_VOLUMEWRITE exports anatomical or functional volume data to a Analyze  
        or BrainVoyager file. The data in the resulting file(s) can be  
        further analyzed and/or visualized in MRIcro, SPM, BrainVoyager,  
        AFNI or similar packages.  
         
        Use as  
          ft_volumewrite(cfg, volume)  
        where the input volume structure should represent an anatomical MRI  
        that was for example obtained from FT_READ_MRI, the source  
        reconstruction results from FT_SOURCEANALYSIS, the statistical  
        results from FT_SOURCESTATISTICS or an otherwise processed anatomical  
        or functional volume.  
         
        The configuration structure should contain the following elements  
          cfg.parameter     = string, describing the functional data to be processed,  
                              e.g. 'pow', 'coh', 'nai' or 'anatomy'  
          cfg.filename      = filename without the extension  
         
        To determine the file format, the following option can be specified  
          cfg.filetype      = 'analyze_old', 'nifti' (default), 'nifti_img', 'analyze_spm',  
                              'nifti_spm', 'nifti_gz', 'mgz', 'mgh', 'vmp' or 'vmr'  
         
        Depending on the filetype, the cfg should also contain  
          cfg.vmpversion    = 1 or 2, version of the vmp format to use (default = 2)  
          cfg.spmversion    = string, version of SPM to be used (default = 'spm12')  
         
        The default filetype is 'nifti', which means that a single *.nii file will be  
        written using code from the freesurfer toolbox. The 'nifti_img' filetype uses SPM  
        for a dual file (*.img/*.hdr) nifti-format file. The 'nifti_spm' filetype uses SPM  
        for a single 'nifti' file.  
         
        The analyze, analyze_spm, nifti, nifti_img, nifti_spm and mgz filetypes support a  
        homogeneous transformation matrix, the other filetypes do not support a homogeneous  
        transformation matrix and hence will be written in their native coordinate system.  
         
        You can specify the datatype for the nifti, analyze_spm and analyze_old  
        formats. If not specified, the class of the input data will be preserved,  
        if the file format allows. Although the higher level function may make an  
        attempt to typecast the data, only the nifti fileformat preserves the  
        datatype. Also, only when filetype = 'nifti', the slope and intercept  
        parameters are stored in the file, so that, when reading the data from  
        file, the original values are restored (up to the bit resolution).  
          cfg.datatype      = 'uint8', 'int8', 'int16', 'int32', 'single' or 'double'  
         
        By default, integer datatypes will be scaled to the maximum value of the  
        physical or statistical parameter, floating point datatypes will not be  
        scaled. This can be modified, for instance if the data contains only integers with  
        indices into a parcellation, by  
          cfg.scaling       = 'yes' or 'no'  
         
        Optional configuration items are  
          cfg.downsample    = integer number (default = 1, i.e. no downsampling)  
          cfg.fiducial.nas  = [x y z] position of nasion  
          cfg.fiducial.lpa  = [x y z] position of LPA  
          cfg.fiducial.rpa  = [x y z] position of RPA  
          cfg.markfiducial  = 'yes' or 'no', mark the fiducials  
          cfg.markorigin    = 'yes' or 'no', mark the origin  
          cfg.markcorner    = 'yes' or 'no', mark the first corner of the volume  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
        If you specify this option the input data will be read from a *.mat  
        file on disk. This mat files should contain only a single variable named 'data',  
        corresponding to the input structure.  
         
        See also FT_SOURCEANALYSIS, FT_SOURCESTATISTICS, FT_SOURCEINTERPOLATE, FT_WRITE_MRI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_volumewrite.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_volumewrite", *args, **kwargs, nargout=0)
