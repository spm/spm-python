from spm.__wrapper__ import Runtime


def ft_volumerealign(*args, **kwargs):
    """
      FT_VOLUMEREALIGN spatially aligns an anatomical MRI with head coordinates based on  
        external fiducials or anatomical landmarks. This function typically does not change  
        the anatomical MRI volume itself, but only adjusts the homogeneous transformation  
        matrix that describes the mapping from voxels to the coordinate system. It also  
        appends a coordsys-field to the output data, or it updates it. This field specifies  
        how the x/y/z-axes of the coordinate system should be interpreted. Occasionally,  
        the orientation and handedness of the output volume may be different from the orientation  
        and handedness of the input volume. This is determined by the cfg.flip  
        argument. See the code for more details.  
         
        For spatial normalisation and deformation (i.e. warping) an MRI to a template brain  
        you should use the FT_VOLUMENORMALISE function.  
         
        Different methods for aligning the anatomical MRI to a coordinate system are  
        implemented, which are described in detail below:  
         
        INTERACTIVE - Use a graphical user interface to click on the location of anatomical  
        landmarks or fiducials. The anatomical data can be displayed as three orthogonal  
        MRI slices or as a rendering of the head surface. The coordinate system is updated  
        according to the definition of the coordinates of these fiducials.  
         
        FIDUCIAL - The coordinate system is updated according to the definition of the  
        coordinates of anatomical landmarks or fiducials that are specified in the  
        configuration.  
         
        HEADSHAPE - Match the head surface from the MRI with a measured head surface using  
        an iterative closest point procedure. The MRI will be updated to match the measured  
        head surface. You can optionally do an initial manual coregistration of the two head  
        surfaces.  
         
        SPM - Align the individual MRI to the coordinate system of a target or template MRI  
        by matching the two volumes.  
         
        FSL - Align the individual MRI to the coordinate system of a target or template MRI  
        by matching the two volumes.  
         
        Use as  
          [mri] = ft_volumerealign(cfg, mri)  
        or  
          [mri] = ft_volumerealign(cfg, mri, target)  
        where the first input is the configuration structure, the second input is an  
        anatomical or functional MRI volume and the third (optional) input is the the  
        target anatomical MRI for SPM or FSL.  
         
        The configuration can contain the following options  
          cfg.method         = string representing the method for aligning  
                               'interactive' use the GUI to specify the fiducials  
                               'fiducial'    use pre-specified fiducials  
                               'headshape'   match the MRI surface to a headshape  
                               'spm'         match to template anatomical MRI  
                               'fsl'         match to template anatomical MRI  
          cfg.coordsys       = string specifying the origin and the axes of the coordinate  
                               system. Supported coordinate systems are 'ctf', '4d', 'bti',  
                               'eeglab', 'neuromag', 'itab', 'yokogawa', 'asa', 'acpc',  
                               and 'paxinos'. See http://tinyurl.com/ojkuhqz  
          cfg.clim           = [min max], scaling of the anatomy color (default is automatic)  
          cfg.parameter      = 'anatomy' the parameter which is used for the visualization  
          cfg.viewresult     = string, 'yes' or 'no', whether or not to visualize aligned volume(s)  
                               after realignment (default = 'no')  
          cfg.flip           = string, 'yes' or 'no', to realign the volume approximately to the   
                               input coordinate axes, this may reorient the output volume relative  
                               to the input (default = 'yes', when cfg.method = 'interactive', and 'no'  otherwise)  
         
        When cfg.method = 'interactive', a user interface allows for the specification of  
        the fiducials or landmarks using the mouse, cursor keys and keyboard. The fiducials  
        can be specified by pressing the corresponding key on the keyboard (n/l/r or  
        a/p/z). When pressing q the interactive mode will stop and the transformation  
        matrix is computed. This method supports the following options:  
          cfg.viewmode    = 'ortho' or 'surface', visualize the anatomical MRI as three  
                             slices or visualize the extracted head surface (default = 'ortho')  
          cfg.snapshot     = 'no' ('yes'), making a snapshot of the image once a  
                             fiducial or landmark location is selected. The optional second  
                             output argument to the function will contain the handles to these  
                             figures.  
          cfg.snapshotfile = 'ft_volumerealign_snapshot' or string, the root of  
                             the filename for the snapshots, including the path. If no path  
                             is given the files are saved to the pwd. The consecutive  
                             figures will be numbered and saved as png-file.  
         
        When cfg.method = 'fiducial' and cfg.coordsys is based on external anatomical  
        landmarks, as is common for EEG and MEG, the following is required to specify the  
        voxel indices of the fiducials:  
          cfg.fiducial.nas    = [i j k], position of nasion  
          cfg.fiducial.lpa    = [i j k], position of LPA  
          cfg.fiducial.rpa    = [i j k], position of RPA  
          cfg.fiducial.zpoint = [i j k], a point on the positive z-axis. This is  
                                an optional 'fiducial', and can be used to determine  
                                whether the input voxel coordinate axes are left-handed  
                                (i.e. flipped in one of the dimensions). If this additional  
                                point is specified, and the voxel coordinate axes are left  
                                handed, the volume is flipped to yield right handed voxel  
                                axes.  
         
        When cfg.method = 'fiducial' and cfg.coordsys = 'acpc', as is common for fMRI,  
        the following is required to specify the voxel indices of the fiducials:  
          cfg.fiducial.ac      = [i j k], position of anterior commissure  
          cfg.fiducial.pc      = [i j k], position of posterior commissure  
          cfg.fiducial.xzpoint = [i j k], point on the midsagittal-plane with a  
                                 positive Z-coordinate, i.e. an interhemispheric  
                                 point above ac and pc  
        The coordinate system will be according to the RAS_Tal convention, i.e.  
        the origin corresponds with the anterior commissure the Y-axis is along  
        the line from the posterior commissure to the anterior commissure the  
        Z-axis is towards the vertex, in between the hemispheres the X-axis is  
        orthogonal to the YZ-plane, positive to the right.  
         
        When cfg.method = 'fiducial' and cfg.coordsys = 'paxinos' for a mouse brain,  
        the following is required to specify the voxel indices of the fiducials:  
          cfg.fiducial.bregma      = [i j k], position of bregma  
          cfg.fiducial.lambda      = [i j k], position of lambda  
          cfg.fiducial.yzpoint     = [i j k], point on the midsagittal-plane  
         
        With the 'interactive' and 'fiducial' methods it is possible to define an  
        additional point (with the key 'z'), which should be a point on the positive side  
        of the xy-plane, i.e. with a positive z-coordinate in world coordinates. This point  
        will subsequently be used to check whether the input coordinate system is left or  
        right-handed. For the 'interactive' method you can also specify an additional  
        control point (with the key 'r'), that should be a point with a positive coordinate  
        on the left-right axis, i.e.', a point on the right of the head.  
         
        When cfg.method = 'headshape', the function extracts the scalp surface from the  
        anatomical MRI, and aligns this surface with the user-supplied headshape.  
        Additional options pertaining to this method should be defined in the subcfg  
        cfg.headshape. The following option is required:  
          cfg.headshape.headshape      = string pointing to a headshape structure or a  
                                         file containing headshape, see FT_READ_HEADSHAPE  
         
        Additional options pertaining to the headshape method should be specified in  
        the sub-structure cfg.headshape and can include:  
          cfg.headshape.scalpsmooth    = scalar, smoothing parameter for the scalp  
                                         extraction (default = 2)  
          cfg.headshape.scalpthreshold = scalar, threshold parameter for the scalp  
                                         extraction (default = 0.1)  
          cfg.headshape.interactive    = 'yes' or 'no', use interactive realignment to  
                                         align headshape with scalp surface (default = 'yes')  
          cfg.headshape.icp            = 'yes' or 'no', use automatic realignment  
                                         based on the icp-algorithm. If both 'interactive'  
                                         and 'icp' are executed, the icp step follows the  
                                         interactive realignment step (default = 'yes')  
         
        When cfg.method = 'spm', a third input argument is required. The input volume is  
        coregistered to this target volume, using SPM. You can specify the version of  
        the SPM toolbox to use with  
          cfg.spmversion       = string, 'spm2', 'spm8', 'spm12' (default = 'spm12')  
         
        Additional options pertaining to SPM2 and SPM8 should be defined in the  
        sub-structure cfg.spm and can include:  
          cfg.spm.regtype      = 'subj', 'rigid'  
          cfg.spm.smosrc       = scalar value  
          cfg.spm.smoref       = scalar value  
         
        Additional options pertaining to SPM12 should be defined in the  
        sub-structure cfg.spm and can include:  
          cfg.spm.sep          = optimisation sampling steps (mm), default: [4 2]  
          cfg.spm.params       = starting estimates (6 elements), default: [0 0 0  0 0 0]  
          cfg.spm.cost_fun     = cost function string:  
                                 'mi'  - Mutual Information (default)  
                                 'nmi' - Normalised Mutual Information  
                                 'ecc' - Entropy Correlation Coefficient  
                                 'ncc' - Normalised Cross Correlation  
          cfg.spm.tol          = tolerences for accuracy of each param, default: [0.02 0.02 0.02 0.001 0.001 0.001]  
          cfg.spm.fwhm         = smoothing to apply to 256x256 joint histogram, default: [7 7]  
         
        When cfg.method is 'fsl', a third input argument is required. The input volume is  
        coregistered to this target volume, using FSL-flirt. Additional options pertaining  
        to the FSL method should be defined in the sub-structure cfg.fsl and can include:  
          cfg.fsl.path         = string, specifying the path to fsl  
          cfg.fsl.costfun      = string, specifying the cost-function used for  
                                 coregistration  
          cfg.fsl.interpmethod = string, specifying the interpolation method, can be  
                                 'trilinear', 'nearestneighbour', or 'sinc'  
          cfg.fsl.dof          = scalar, specifying the number of parameters for the  
                                 affine transformation. 6 (rigid body), 7 (global  
                                 rescale), 9 (traditional) or 12.  
          cfg.fsl.reslice      = string, specifying whether the output image will be  
                                 resliced conform the target image (default = 'yes')  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a  
        *.mat file on disk and/or the output data will be written to a *.mat  
        file. These mat files should contain only a single variable,  
        corresponding with the input/output structure.  
         
        See also FT_READ_MRI, FT_VOLUMERESLICE, FT_INTERACTIVEREALIGN, FT_ELECTRODEREALIGN,  
        FT_DETERMINE_COORDSYS, SPM_AFFREG, SPM_NORMALISE, SPM_COREG  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_volumerealign.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_volumerealign", *args, **kwargs)
