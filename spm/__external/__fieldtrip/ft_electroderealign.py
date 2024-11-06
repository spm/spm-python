from spm.__wrapper__ import Runtime


def ft_electroderealign(*args, **kwargs):
    """
      FT_ELECTRODEREALIGN rotates, translates, scales and warps electrode positions. The  
        default is to only rotate and translate, i.e. to do a rigid body transformation in  
        which only the coordinate system is changed. With the right settings if can apply  
        additional deformations to the input sensors (e.g. scale them to better fit the  
        skin surface). The different methods are described in detail below.  
         
        INTERACTIVE - You can display the skin surface together with the electrode or  
        gradiometer positions, and manually (using the graphical user interface) adjust the  
        rotation, translation and scaling parameters, so that the electrodes correspond  
        with the skin.  
         
        FIDUCIAL - You can apply a rigid body realignment based on three fiducial  
        locations. After realigning, the fiducials in the input electrode set (typically  
        nose, left and right ear) are along the same axes as the fiducials in the template  
        electrode set.  
         
        TEMPLATE - You can apply a spatial transformation/deformation that automatically  
        minimizes the distance between the electrodes or gradiometers and a template or  
        sensor array. The warping methods use a non-linear search to minimize the distance  
        between the input sensor positions and the corresponding template sensors.  
         
        HEADSHAPE - You can apply a spatial transformation/deformation that automatically  
        minimizes the distance between the electrodes and the head surface. The warping  
        methods use a non-linear search to minimize the distance between the input sensor  
        positions and the projection of the electrodes on the head surface.  
         
        PROJECT - This projects each of the electrodes to the nearest point on the  
        head surface mesh.  
         
        MOVEINWARD - This moves all electrodes inward according to their normals.  
         
        MNI - This transforms the electrodes nonlinearly using the same transformation of  
        the individual anatomical MRI to the MNI template.  
         
        Use as  
          [elec_realigned] = ft_electroderealign(cfg)  
        with the electrode or gradiometer details in the configuration, or as  
          [elec_realigned] = ft_electroderealign(cfg, elec_orig)  
        with the electrode or gradiometer definition as 2nd input argument.  
         
        The configuration can contain the following options  
          cfg.method         = string representing the method for aligning or placing the electrodes  
                               'interactive'     realign manually using a graphical user interface  
                               'fiducial'        realign using three fiducials (e.g. NAS, LPA and RPA)  
                               'template'        realign the electrodes to match a template set  
                               'headshape'       realign the electrodes to fit the head surface  
                               'project'         projects electrodes onto the head surface  
                               'moveinward'      moves electrodes inward along their normals  
                               'mni'             transforms electrodes from individual subject to MNI space  
          cfg.warp          = string describing the spatial transformation for the template and headshape methods  
                               'rigidbody'       apply a rigid-body warp (default)  
                               'globalrescale'   apply a rigid-body warp with global rescaling  
                               'traditional'     apply a rigid-body warp with individual axes rescaling  
                               'nonlin1'         apply a 1st order non-linear warp  
                               'nonlin2'         apply a 2nd order non-linear warp  
                               'nonlin3'         apply a 3rd order non-linear warp  
                               'nonlin4'         apply a 4th order non-linear warp  
                               'nonlin5'         apply a 5th order non-linear warp  
                               'dykstra2012'     back-project ECoG onto the cortex using energy minimzation  
                               'hermes2010'      back-project ECoG onto the cortex along the local norm vector  
                               'fsaverage'       surface-based realignment with FreeSurfer fsaverage brain (left->left or right->right)  
                               'fsaverage_sym'   surface-based realignment with FreeSurfer fsaverage_sym left hemisphere (left->left or right->left)  
                               'fsinflated'      surface-based realignment with FreeSurfer individual subject inflated brain (left->left or right->right)  
          cfg.channel        = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details  
          cfg.keepchannel    = string, 'yes' or 'no' (default = 'no')  
          cfg.fiducial       = cell-array with the name of three fiducials used for realigning (default = {'nasion', 'lpa', 'rpa'})  
          cfg.casesensitive  = 'yes' or 'no', determines whether string comparisons between electrode labels are case sensitive (default = 'yes')  
          cfg.feedback       = 'yes' or 'no' (default = 'no')  
         
        The electrode positions can be present in the 2nd input argument or can be specified as  
          cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS  
         
        If you want to realign the EEG electrodes using anatomical fiducials, you should  
        specify the target location of the three fiducials, e.g.  
          cfg.target.pos(1,:) = [110 0 0]     % location of the nose  
          cfg.target.pos(2,:) = [0  90 0]     % location of the left ear  
          cfg.target.pos(3,:) = [0 -90 0]     % location of the right ear  
          cfg.target.label    = {'NAS', 'LPA', 'RPA'}  
         
        If you want to align EEG electrodes to a single or multiple template electrode sets  
        (which will be averaged), you should specify the template electrode sets either as  
        electrode structures (i.e. when they are already read in memory) or their file  
        names using  
          cfg.target          = single electrode set that serves as standard  
        or  
          cfg.target{1..N}    = list of electrode sets that will be averaged  
         
        If you want to align EEG electrodes to the head surface, you should specify the head surface as  
          cfg.headshape      = a filename containing headshape, a structure containing a  
                               single triangulated boundary, or a Nx3 matrix with surface  
                               points  
         
        If you want to align ECoG electrodes to the pial surface, you first need to compute  
        the cortex hull with FT_PREPARE_MESH. Then use either the algorithm described in  
        Dykstra et al. (2012, Neuroimage) or in Hermes et al. (2010, J Neurosci methods) to  
        snap the electrodes back to the cortical hull, e.g.  
          cfg.method         = 'headshape'  
          cfg.warp           = 'dykstra2012', or 'hermes2010'  
          cfg.headshape      = a filename containing headshape, a structure containing a  
                               single triangulated boundary, or a Nx3 matrix with surface  
                               points  
          cfg.feedback       = 'yes' or 'no' (default), feedback of the iteration procedure  
         
        Additional configuration options for cfg.warp='dykstra2012'  
          cfg.maxiter        = number (default: 50), maximum number of optimization iterations  
          cfg.pairmethod     = 'pos' (default) or 'label', the method for electrode  
                               pairing on which the deformation energy is based  
          cfg.isodistance    = 'yes', 'no' (default) or number, to enforce isotropic  
                               inter-electrode distances (pairmethod 'label' only)  
          cfg.deformweight   = number (default: 1), weight of deformation relative  
                               to shift energy cost (lower increases grid flexibility)  
         
        If you want to move the electrodes inward, you should specify  
          cfg.moveinward     = number, the distance that the electrode should be moved  
                               inward (negative numbers result in an outward move)  
         
        If you want to align ECoG electrodes to the freesurfer average brain, you should  
        specify the path to your headshape (e.g., lh.pial), and ensure you have the  
        corresponding registration file (e.g., lh.sphere.reg) in the same directory.  
        Moreover, the path to the local freesurfer home is required. Note that, because the  
        electrodes are being aligned to the fsaverage brain, the corresponding brain should  
        be also used when plotting the data, i.e. use freesurfer/subjects/fsaverage/surf/lh.pial  
        rather than surface_pial_left.mat  
          cfg.method         = 'headshape'  
          cfg.warp           = 'fsaverage'  
          cfg.headshape      = string, filename containing subject headshape (e.g. <path to freesurfer/surf/lh.pial>)  
          cfg.fshome         = string, path to freesurfer  
         
        If you want to transform electrodes from individual subject coordinates to MNI  
        space, you should specify the following  
          cfg.mri            = structure with the individual anatomical MRI relative to which electrodes are specified, or the filename of the MRI, see FT_READ_MRI  
          cfg.templatemri    = string, filename of the MNI template (default = 'T1.mnc' for SPM2 or 'T1.nii' for SPM8 and SPM12)  
          cfg.spmversion     = string, 'spm2', 'spm8', 'spm12' (default = 'spm12')  
          cfg.spmmethod      = string, 'old', 'new' or 'mars', see FT_VOLUMENORMALISE  
          cfg.nonlinear      = string, 'yes' or 'no', see FT_VOLUMENORMALISE  
         
        See also FT_READ_SENS, FT_VOLUMEREALIGN, FT_INTERACTIVEREALIGN,  
        FT_DETERMINE_COORDSYS, FT_PREPARE_MESH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_electroderealign.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_electroderealign", *args, **kwargs)
