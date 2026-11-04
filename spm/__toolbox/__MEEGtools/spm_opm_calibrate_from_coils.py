from spm._runtime import Runtime


def spm_opm_calibrate_from_coils(*args, **kwargs):
    r"""
        [cal_D, positions] = spm_opm_calibrate_from_coils(S) estimates   
          the 3D positions, orientations, and gains of magnetometers based on   
          recordings during external coil activation. The function fits observed   
          signals to a model of magnetic dipoles using both amplitude and phase   
          errors. Results are then used to calibrate the magnetometer array.  
                     
          Input:  
              S : structure with fields  
                  - D:               MEEG D object to be calibrated (required)  
                  - freq:            Coil signal frequency in Hz (default: 10)  
                  - chan_name_format Format of sensor/axis for channel (default:  
                                     '^(X|Y|Z)(.*?)$'  
                  - amplitude_range: 1x2 [min max] amplitude range (fT) for filtering  
                                     (default: [0.1 1000]*1e3)  
                  - coil_properties: structure with fields:  
                      positions:     n x 3 dipole positions (m)  
                      orientations:  n x 3 dipole unit vector  
                      resistance:    default, 2120  
                      inner_r:       default, 3.68/1000 (m)  
                      outer_r:       default, 10.94/1000 (m)  
                      layers:        default, 6  
                      layer_turns:   default, 45  
                  - t_delay:         timing offset for phase correction (ms),   
                                     default: 'auto')  
                  - phase_tol:       tolerance for phase filter applied (rads),   
                                     default: 'auto')  
                  - coil_trigger:    structure with fields:  
                      event_channel: channel name for triggers (default: 'A8')  
                      event_design:  order of coil operations. (default:   
                                     repmat(1:16,[1 4]). Index with respect to  
                                     coil_properies.  
                      event_duration:in seconds (default: 1);  
                      event_trim:    1 x 2, seconds to trim from [start, end].  
                                     (default: [1/S.freq, 1/S.freq])  
                      signal_channel:channel name for coil signals (default: 'A16')  
                  - plot_output:     boolean  
                  - highpass:        highpass filter freq (Hz), default 5  
                  - channels:        cell array of channels. If empty, include all  
                  - use_similarity   boolean, whether to use starting parameters  
                                     based on similar observations across  
                                     channels, default: true;  
                  - fast             boolean, skip permutations where possible  
                                     due to good starting conditions. Set to  
                                     false if bad channels are missed, (default:  
                                     true)  
                  - prescale         boolean, apply initial gain estimate (useful  
                                     for highly deviant (uncalibrated) channels).  
                                     Note that gain visualisation will be wrong.  
                                     Probably redundant with analytic gain solve  
                  - balance          boolean, update existing forward model/s,   
                                     (default: false)  
                  - estimation: structure with fields:  
                      permutations:  number of permutations to run (default: 6)  
                      min_ops:       minimum number of valid operations to  
                                     estimate axis (default: 8)  
                      sub_sel_num:   number of operations to estimate for initial   
                                     estimate/s (default: 5)  
                      phase_tol:     tolerance for phase filter (default: 'auto')  
                      pos_bounds:    lower/upper bounds per dimension (m) (default:  
                                     [-0.15, 0.15; -0.15, 0.15; -0.3, -0.05]  
                      gain_bounds:   [0.666, 1.5];  
                      parallel:      boolean, use parallel processing, default  
                                     false  
                      bootstrap:     number of bootstrap samples (default: 0,  
                                     i.e. no bootstrap)  
                  - output_filename: filename for saving table;  
         
          Output:  
              cal_D:                 calibrated D object (spm_opm_apply_calibration)  
              positions: table containing calibrated sensor information  
                  - name:        sensor/channel name  
                  - Px, Py, Pz:  position coordinates (mm)  
                  - Ox, Oy, Oz:  orientation vector components  
                  - gain:        channelwise gain factor  
                  - cal_error:   calibration error (RMS)  
                  (optional, if bootstrap > 0)  
                  - std_pos:     bootstrap SE of distance from optimal position (mm)  
                  - std_ori:     bootstrap SE of angular deviation from optimal  
                                 orientation vector (degrees)  
                  - std_gain     bootstrap SE of gain  
         
          Example usage:  
              % Load file with HALO activation  
              S = [];  
              S.data = 'D:\data\sub-1_ses-1_task-halo_run-1_meg.lvm';  
              D = spm_opm_create(S);  
              % Calibrate  
              S = [];  
              S.D = D;  
              [cal_D, positions] = spm_opm_calibrate_from_coils(S);  
              % Load data from experiment (ensure no recalibration after HALO)  
              S = [];  
              S.data = 'D:\data\sub-1_ses-1_task-experiment_run-1_meg.lvm';  
              D2 = spm_opm_create(S);  
              % Apply calibration to data from experiment  
              S = [];  
              S.D = D2;  
              S.positions = positions;  
              [cal_D2] = spm_opm_apply_calibration(S)  
            
          Notes:  
              The cal_error is reported per axis, but the optimisation is based on   
                  a combined cal_error term for all 'good' axes in a sensor.  
              cal_error is the RMS of amplitude error between modelled and observed   
                  responses. No threshold is set other than successful fit relative   
                  to other axes and passing input tests. Set estimation.bootstrap   
                  to get sensitivity estimate.   
              See Hill et al. (2025) https://doi.org/10.1162/imag_a_00535 for   
                  details on the HALO system (Quspin Inc. CO, USA) used as the   
                  default parameters in this function.  
              Several steps are taken to ensure only good data goes into the  
                  estimation, including checking phase consistency, amplitude  
                  correlation, amplitude thresholding, and removal of axes not  
                  contributing to the fit.  
         
        Author: Nicholas Alexander (n.alexander@ucl.ac.uk)  
        Copyright: Department of Imaging Neuroscience, UCL, 2026  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_opm_calibrate_from_coils.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opm_calibrate_from_coils", *args, **kwargs)
