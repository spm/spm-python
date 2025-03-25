"""
analyse some ERP data (mismatch negativity ERP SPM file from SPM-webpages)
This is an example batch script to analyse two evoked responses with an
assumed 5 sources.
To try this out on your data (the date of this example don't exist in your SPM8 distribution),
you have to change 'Pbase' to your own analysis-directory, and choose a name ('DCM.xY.Dfile')
of an existing SPM for M/EEG-file with at least two evoked responses.
"""

import os
import spm

num = spm.Array.from_any

# Please replace filenames etc. by your own.
# ----------------------------------------------------------------------
spm.spm("defaults", "EEG")

# Data and analysis directories
# ----------------------------------------------------------------------

Pbase = os.path.dirname(__file__)  # directory with your data,

Pdata = os.path.join(Pbase, ".")  # data directory in Pbase
Panalysis = os.path.join(Pbase, ".")  # analysis directory in Pbase

os.chdir(Pbase)

# Data filename
# ----------------------------------------------------------------------
DCM = spm.Struct()
DCM.xY.Dfile = "maeMdfspm8_subject1"

# Parameters and options used for setting up model
# ----------------------------------------------------------------------
DCM.options.analysis = "ERP"  # analyze evoked responses
DCM.options.model = "ERP"  # ERP model
DCM.options.spatial = "IMG"  # spatial model
DCM.options.trials = num([1, 2])  # index of ERPs within ERP/ERF file
DCM.options.Tdcm[0] = 0  # start of peri-stimulus time to be modelled
DCM.options.Tdcm[1] = 200  # end of peri-stimulus time to be modelled
DCM.options.Nmodes = 8  # nr of modes for data selection
DCM.options.h = 1  # nr of DCT components
DCM.options.onset = 60  # selection of onset (prior mean)
DCM.options.D = 1  # downsampling

# ----------------------------------------------------------------------
# Data and spatial model
# ----------------------------------------------------------------------
DCM = spm.spm_dcm_erp_data(DCM)

# ----------------------------------------------------------------------
# Location priors for dipoles
# ----------------------------------------------------------------------
DCM.Lpos = num(
    [[-42, -22, 7], [46, -14, 8], [-61, -32, 8], [59, -25, 8], [46, 20, 8]]
).T
DCM.Sname = ["left AI", "right A1", "left STG", "right STG", "right IFG"]
Nareas = DCM.Lpos.shape[1]

# ----------------------------------------------------------------------
# Spatial model
# ----------------------------------------------------------------------
DCM = spm.spm_dcm_erp_dipfit(DCM)

# ----------------------------------------------------------------------
# Specify connectivity model
# ----------------------------------------------------------------------
os.chdir(Panalysis)

DCM.A = spm.Cell()
DCM.B = spm.Cell()

DCM.A[0] = spm.Array(Nareas, Nareas)
DCM.A[0][2, 0] = 1
DCM.A[0][3, 1] = 1
DCM.A[0][4, 3] = 1

DCM.A[1] = spm.Array(Nareas, Nareas)
DCM.A[1][0, 2] = 1
DCM.A[1][1, 3] = 1
DCM.A[1][3, 4] = 1

DCM.A[2] = spm.Array(Nareas, Nareas)
DCM.A[2][3, 2] = 1
DCM.A[2][2, 3] = 1

DCM.B[0] = DCM.A[0] + DCM.A[1]
DCM.B[0][0, 0] = 1
DCM.B[0][1, 1] = 1

DCM.C = num([[1, 1, 0, 0, 0]]).T

# ----------------------------------------------------------------------
# Between trial effects
# ----------------------------------------------------------------------
DCM.xU.X = num([[0, 1]]).T
DCM.xU.name = ["rare"]

# ----------------------------------------------------------------------
# Invert
# ----------------------------------------------------------------------
DCM.name = "DCMexample"

DCM = spm.spm_dcm_erp(DCM)
